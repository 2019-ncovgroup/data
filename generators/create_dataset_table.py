#
# A program to output (to standard output) text to place in the dataset table
#
# Notes:
# 1) It needs to be adjusted to reflect final directory contents. E.g., it assumes
#    just two levels of directories, like, images/HOP/*.csv, and that they only data files
# 2) You need to run some Globus commands to populate files with Petrel information
# 3) The "test" variable needs to be set to False
#
#
# Start with the following, although here and also in "prefix" below, "data" should become v1.0 or similar:

#
# Example line:
# DATA	file	covid19	2020-04-03 16:12:39+00:00	None	None	None	None	None	DUDE	2770	3	dir	petrel

import pandas as pd

debug = 0
test  = True
prefix = 'https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=/data'
types = ['smiles', 'fingerprints', 'fingerprints', 'images']

def scale(number):
    if number < 1000:
        return('%d B'%number)
    for (code, factor) in zip(['-', 'K', 'M', 'G'], range(1, 5)):
        if number/(1000**factor) < 1:
            return('%d %sB'%(int(number/(1000**(factor-1))), code))

def retrieve_data(type):
    df = pd.read_table('%s-ls.tsv'%type)
    df.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'Name', 'K', 'Size', 'Type', 'N']

    dirs  = df[df.Type=='dir']
    files = df[df.Type=='file']
    outputs = {}

    # For each directory:
    for dir in list(dirs.Name):
        if test:
            if dir != 'SAVI' and dir != 'REP':
                continue
        # Find files that are in that directory, i.e., a NAME like DIR/*
        dirfiles = files[files.Name.str.contains('%s/'%dir)]
        numbytes = 0
        for (file, size) in zip(list(dirfiles.Name), list(dirfiles.Size)):
            numbytes += int(size)
        if debug>0:
            print('Directory %s has %d files and %d bytes'%(dir, len(dirfiles), numbytes))
        outputs[dir] = (len(dirfiles), numbytes)

    return(outputs)

def print_table(directories, values):
    for dir in directories:
        outstring = '%s | '%dir
        for (type, vals) in values:
            try:
                (numfiles, numbytes) = vals[dir]
                outstring += '[%d file%s, %s](%s/%s/%s/) | '%(numfiles,\
                              '' if numfiles==1 else 's', scale(numbytes), prefix, type, dir)
            except:
                outstring += 'TBD | '
        print(outstring)

def retrieve_values(type):
    vals = retrieve_data(type)
    if debug>0:
        print('%s:'%type, vals)
    directories = [key for key in vals]
    return((directories, vals))

all_dirs = []
all_vals = []
for type in types:
    (dirs, vals) = retrieve_values(type)
    all_dirs += dirs
    all_vals += [(type, vals)]

unique_dirs = sorted(list(set(all_dirs)))

print_table(unique_dirs, all_vals)


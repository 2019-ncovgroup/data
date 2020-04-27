#
# A program to output (to standard output) text to place in the dataset table
#
# Notes:
#   First run the following Globus commands
"""
globus ls -F unix -l -r a386b552-6086-11ea-9688-0e56c063f437:release/v1.0/canonical_smiles > canonical_smiles-ls.tsv
globus ls -F unix -l -r a386b552-6086-11ea-9688-0e56c063f437:release/v1.0/descriptors > descriptors-ls.tsv
globus ls -F unix -l -r a386b552-6086-11ea-9688-0e56c063f437:release/v1.0/fingerprints > fingerprints-ls.tsv
globus ls -F unix -l -r a386b552-6086-11ea-9688-0e56c063f437:release/v1.0/images > images-ls.tsv
"""
#
# Example line:
# DATA	file	covid19	2020-04-03 16:12:39+00:00	None	None	None	None	None	DUDE	2770	3	dir	petrel

import pandas as pd
import argparse, os

debug = 0

prefix = 'https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=/release/v1.0'
types = ['canonical_smiles', 'fingerprints', 'descriptors', 'images']

def scale(number, B):
    if number < 1000:
        return('%d %s'%(number,B))
    for (code, factor) in zip(['-', 'K', 'M', 'G', 'T'], range(1, 6)):
        if number/(1000**factor) < 1:
            return('%d %s%s'%(int(number/(1000**(factor-1))), code, B))

def remove_nested_dirs(dirs):
    out = []
    for dir in dirs:
        if '/' not in dirs:
            out.append(dir)
    return out

def retrieve_data(type):
    try:
        df = pd.read_table('%s-ls.tsv'%type, header=None)
    except:
        print('FAIL on read of','%s-ls.tsv'%type)
        exit(1)
    df.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'Name', 'K', 'Size', 'Type', 'N']

    dirs1 = df[df.Type=='dir']
    dirs  = dirs1[~dirs1.Name.str.contains('/missing')]
    files = df[df.Type=='file']
    outputs = {}

    if debug>0:
        print('Directories in %s'%type, list(dirs.Name))

    # Removes SAV, etc., in the case of descriptors
    no_subdirs = dirs[~dirs.Name.str.contains('/')]

    # For each directory:
    for dir in list(no_subdirs.Name):
        # Find files that are in that directory, i.e., a NAME like DIR/*
        subdirs  = dirs[dirs.Name.str.contains('%s/'%(dir))]
        subdirnames  = list(dirs[dirs.Name.str.contains('%s/'%(dir))].Name)
        if subdirnames != []:
            if debug>0:
                print('Subdirectories in %s: %s'%(dir, subdirnames))
            numbytes = 0
            numfiles = 0
            for subdirname in subdirnames:
                subdirfiles = files[files.Name.str.contains('%s'%(subdirname))]
                for (file, size) in zip(list(subdirfiles.Name), list(subdirfiles.Size)):
                    numbytes += int(size)
                numfiles += len(subdirfiles)
            outputs[dir] = (numfiles, numbytes)
        else:
            dirfiles1 = files[files.Name.str.contains('%s/'%dir)]
            dirfiles = dirfiles1[~dirfiles1.Name.str.contains('missing')]
            numbytes = 0
            for (file, size) in zip(list(dirfiles.Name), list(dirfiles.Size)):
                numbytes += int(size)
            if debug>0:
                print('Directory %s has %d files and %d bytes'%(dir, len(dirfiles), numbytes))
            outputs[dir] = (len(dirfiles), numbytes)
    return(outputs)

def num(n):
   return( '{:,d}'.format(n) )

def print_table(md_file, lt_file, directories, values):
    total_bytes = {}
    total_files = {}
    for type in types:
        total_bytes[type] = 0
        total_files[type] = 0
    for dir in directories:
        outstring_md = '%s '%dir
        outstring_lt = '%s '%dir
        for (type, vals) in values:
            try:
                (numfiles, numbytes) = vals[dir]
                outstring_md += ' | [%s file%s; %s](%s/%s/%s/) '%(num(numfiles),\
                                '' if numfiles==1 else 's', scale(numbytes, 'B'), prefix, type, dir)
                outstring_lt += ' & %s file%s; %s '%(num(numfiles),\
                                '' if numfiles==1 else 's', scale(numbytes, 'B'))
            except:
                outstring_md += ' | TBD '
                outstring_lt += ' & TBD '
            total_bytes[type] += numbytes
            total_files[type] += numfiles
        #print(outstring_md)
        outstring_lt += '\\\\'
        md_file.write('%s\n'%outstring_md)
        lt_file.write('%s\n'%outstring_lt)

    # Construct final (TOTAL) line for table, and write to outfile. Descriptor and image file counts are scaled.
    outstring_md = '**Total** | '
    outstring_lt = '\\textbf{Total} '
    for type in types:
        if type=='descriptors' or type=='images':
            outstring_md += '[**%s files; %s**](%s/%s) | '%(scale(total_files[type], ''),\
                             scale(total_bytes[type], 'B'), prefix, type)
            outstring_lt += '& \\textbf{%s files; %s} '%(scale(total_files[type], ''),\
                             scale(total_bytes[type], 'B'))
        else:
            outstring_md += '[**%s files; %s**](%s/%s) | '%(num(total_files[type]),\
                             scale(total_bytes[type], 'B'), prefix, type)
            outstring_lt += '& \\textbf{%s files; %s} '%(num(total_files[type]),\
                             scale(total_bytes[type], 'B'))
    #print(outstring_md)
    outstring_lt += '\\\\'
    md_file.write('%s\n'%outstring_md)
    lt_file.write('%s\n'%outstring_lt)

def retrieve_values(type):
    vals = retrieve_data(type)
    if debug>0:
        print('%s:'%type, vals)
    directories = [key for key in vals]
    return((directories, vals))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Program to generate the second table on nCoV web page.')
    parser.add_argument('-D', '--definitions', help='definitions file', default='DEFINITIONS.csv')
    parser.add_argument('-U', '--uniques', help='uniques file', default='UNIQUES.csv')
    parser.add_argument('-o', '--output', help='output directory', default='outputs')
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    md_file = open('%s/table2.md'%args.output, 'w')
    lt_file = open('%s/table2.tex'%args.output, 'w')

    all_dirs = []
    all_vals = []
    for type in types:
        (dirs, vals) = retrieve_values(type)
        all_dirs += dirs
        all_vals += [(type, vals)]

    unique_dirs = sorted(list(set(all_dirs)))
    if debug>0:
        print(unique_dirs)

    print_table(md_file, lt_file, unique_dirs, all_vals)


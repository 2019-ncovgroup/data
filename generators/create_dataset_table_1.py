#
# A program to output (to standard output) text to place in first dataset table
#
# It reads:
# 1) DEFINITIONS.csv
# 2) UNIQUES.csv

import pandas as pd
import argparse, os

def num(n):
   return( '{:,d}'.format(n) )
 

def extract_string_and_url(d):
    s = d.split(']')
    n = s[0]
    if len(s) > 1:
        u = s[1]
    else:
        u = ''
    n = n.replace('[', '')
    u = u.replace('(', '').replace(')', '')
    return(n, u)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Program to generate the first table on nCoV web page.')
    parser.add_argument('-D', '--definitions', help='definitions file', default='DEFINITIONS.csv')
    parser.add_argument('-U', '--uniques', help='uniques file', default='UNIQUES.csv')
    parser.add_argument('-o', '--output', help='output directory', default='outputs')
    args = parser.parse_args()

    definitions = pd.read_csv(args.definitions, header=None)
    definitions.columns = ['Key', 'Definition']
    unique_info = pd.read_csv(args.uniques, header=None)
    unique_info.columns = ['Key', 'Total', 'Unique']

    full = pd.merge(definitions, unique_info, on="Key")

    os.makedirs(args.output, exist_ok=True)

    md_file = open('%s/table1.md'%args.output, 'w')
    lt_file = open('%s/table1.tex'%args.output, 'w')

    grand_total = 0
    for key, definition, total, unique in zip(list(full.Key), list(full.Definition), list(full.Total), list(full.Unique)):
        outstring_md = '%s | %s | %s | %0.1f'%(key, definition, num(total), int(unique)*100.0/int(total))
        (defn, url) = extract_string_and_url(definition)
        if url=='':
            def_string = defn
        else:
            def_string = '\\href{%s}{%s}'%(url, defn)
        outstring_lt = '%s & %s & %s & %0.1f\\\\'%(key, def_string, num(total), int(unique)*100.0/int(total))
        grand_total += int(total)
        #print(outstring_md)
        md_file.write('%s\n'%outstring_md)
        lt_file.write('%s\n'%outstring_lt)
    outstring_md = '**Total** | | **%s** | '%num(grand_total)
    outstring_lt = '\\textbf{Total} & &  \\textbf{%s} & '%num(grand_total)
    #print(outstring_md)
    md_file.write('%s\n'%outstring_md)
    lt_file.write('%s\n'%outstring_lt)
 


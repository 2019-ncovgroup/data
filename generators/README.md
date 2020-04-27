# Code to generate tables for web page and document

The programs `create_dataset_table_1.py` and `create_dataset_table_2.py` generate Markdown and Latex content for the two tables on the nCoV web site.

## Create table 1

To run:
```
python create_dataset_table_1.py
```

This reads content from two files:

* `DEFINITIONS.csv`: A KEY,[DESCRIPTION](URL) line for each dataset. Manually created.

* `UNIQUES.csv`: A KEY,NUM-LINES,NUM-UNIQUES line for each dataset, where NUM-UNIQUES is the number of records that occur in no other dataset. Created via query to PostGres database.

It writes two files, `table1.md` and `table1.tex`, in the `outputs` directory.

Its optional `-o`, `-D`, and `-U' arguments allows you to change the name of the output directory and the two input files.

## Create table 2

To run:
```
python create_dataset_table_2.py
```

This program reads contents from four files that should previously have been generated via Globus commands as follows:

```
globus ls -F unix -l -r a386b552-6086-11ea-9688-0e56c063f437:data/smiles > smiles-ls.tsv
globus ls -F unix -l -r a386b552-6086-11ea-9688-0e56c063f437:data/descriptors > descriptors-ls.tsv
globus ls -F unix -l -r a386b552-6086-11ea-9688-0e56c063f437:data/fingerprints > fingerprints-ls.tsv
globus ls -F unix -l -r a386b552-6086-11ea-9688-0e56c063f437:data/images > images-ls.tsv
```

It writes two files, `table2.md` and `table2.tex`, in the `outputs` directory.

Its optional `-o` argument allows you to change the name of the output directory.

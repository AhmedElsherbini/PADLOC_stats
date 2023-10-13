# PADLOC_stats

**What is this script?**

[PADLOC](https://github.com/padlocbio/padloc) is a great tool for antiviral defence locator. However, if you used it for many genomes, and you want to summarize the many basic summary (_padloc.csv) stats into an overview Excel sheet, then this simple Python3 script shall do this job.


**What do you need?**

You shall have the pad_loc.csv files in one folder and these dependencies (pandas, openpyxl ,glob,and argparse)

Just type this command and you will get two Excel sheets in the same folder of your csv files.

"-i /--input_dir"  is your path to the directory of csv files 

"-p /--prefix"  is your preferred prefix for your run

```python
 python padloc_stats.py -i ./txt -p Corynebacterium
```

**What do you get?**


Currently, two Excel files.

1- "prefix"_frequency.xlsx (The general one).

Here you have the "frequency" of each system in your genomes and a relative frequency. Well, the relative frequency is the outcome of dividing the frequency/ number of genomes.


2- "prefix"_presence absence.xlsx  (The detailed one).

It is a matrix, with a presence or absence (1/0) of each system in each genome. Very good to fit in heatmaps.

Thanks

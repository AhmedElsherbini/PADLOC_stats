# PADLOC_stats

**What is this script?**

[PADLOC](https://github.com/padlocbio/padloc) is a great tool for antiviral defense systems locator. However, if you used it for many genomes, and you want to summarize the many basic summary (_padloc.csv) stats into an overview Excel sheet, then this simple Python3 script shall do this job.


**What do you need?**
ImportantL I have developed this script in python 3.9.

You shall have the _padloc.csv files in one folder and these dependencies (pandas, openpyxl ,glob,and argparse)

Just type this command and you will get two Excel sheets in the same folder of your CSV files.

"-i /--input_dir"  is your path to the directory of CSV files 

"-p /--prefix"  is your preferred prefix for your run

```python
 python padloc_stats.py -i ./txt -p Corynebacterium
```

**What do you get?**

Currently, two CSV files.

1- "prefix"_frequency.csv (The general one like a summary of systems per the whole run).

Here you have the "frequency" of each system in your genomes and a relative frequency. Well, what is the relative frequency? The relative frequency is the outcome of dividing the frequency/ number of genomes.


2- "prefix"_presence absence.csv  (The more detailed one).

It is a matrix, with a presence or absence (1/0) of each system in each genome. Very good to fit in heatmaps in the next section.

**What about visualization?**

Well, nothing better than R for this, a simple (and redundant) example for heatmap exists in the defensome.R


Thanks

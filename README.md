# PADLOC_stats

**What is this script?**

[PADLOC](https://github.com/padlocbio/padloc) is a great tool for antiviral defence locator. However, if you used it for many genomes, and you want to merge the basic summary (_padloc.csv) stats  into one Excel sheet, then this simple Python3 script shall do this job.


**What do you need?**

You shall have the summary.txt files in one folder and these dependencies (pandas, openpyxl ,and argparse)

Just type this command and you will get two Excel sheets in the same folder of your txt files.

"-i /--input_dir"  is your path to the directory of txt files 

"-p /--prefix"  is your preferred prefix for this work

```python
 python padloc_stats.py -i ./txt -p Corynebacterium
```

Thanks

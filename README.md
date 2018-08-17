# DFIO

Command line utility to load a CSV into a dataframe, execute some (fairly simple) pandas command and return a result/make a plot.

```
   Options:
          -d Delimiter
          -e Execute this command (give everything following 'df.')
          -p Set to make a plot (plots to 'out.png')
          -h Print help message
   
   Example:
           $ dfio -d '\t' -e 'sepal_length.mean()' iris.tsv
           5.843
```

Sample.py, samples a given fraction of a file.
```
  usage: sample.py [-h] -f FRACTION [--header] filename

  Sample some fraction of a the rows of a file

  positional arguments:
    filename

  optional arguments:
    -h, --help            show this help message and exit
    -f FRACTION, --fraction FRACTION
                          Fraction of file to be returned
    --header
```

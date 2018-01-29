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


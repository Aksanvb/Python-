##Pandas :
##    Pandas is a python library used for working data sets.
##    the name is derived from the word "panel data"
##    it has functions for analyzing, cleaning and manipulating data.

##pip install openpyxl
##Pandas datastructure
##     *Series
##     *saving dataframe

##DataFrame :
##    data frame is a combination of rows and columns. it is a 2d data structure
##    and size is mutable
##    tabular data

##Series :
##    A pandas series is like a column in a table. it is a 1d array holding data
##    of any type

##import pandas
##a=[1,2,3,4,5]
##b=pandas.Series(a)
##print(b)

##import pandas as pd
##a=[70,65,80]
##b=pd.Series(a,index=(["tamil","english","maths"]))
##print(b)

##import pandas as pd
##a={"name" : ["sam","ram"],
##   "age" : [25,26],
##   "address" : ["chennai","trichy"]}
##b=pd.DataFrame(a)
##b["mobile no"]=[1234567890,9876543210]
##b.to_csv("sample1.csv")
##c=pd.read_csv("sample1.csv")
##print(c)

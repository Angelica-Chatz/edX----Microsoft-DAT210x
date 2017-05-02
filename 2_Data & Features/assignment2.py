import pandas as pd

# TODO: Load up the 'tutorial.csv' dataset
#
df=pd.read_csv('tutorial.csv')



print(df)



# TODO: Print the results of the .describe() method
#
df.describe(include='all')



# TODO: Figure out which indexing method you need to
# use in order to index your dataframe with: [2:4,'col3']
# And print the results

df.loc[2:4,'col3']
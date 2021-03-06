import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import parallel_coordinates

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')



# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'

df = pd.read_csv('wheat.data')




# TODO: Drop the 'id' feature, if you included it as a feature
# (Hint: You shouldn't have)
# Also get rid of the 'area' and 'perimeter' features

df.drop(df.columns[[0,1,2]], axis=1, inplace=True)


# TODO: Plot a parallel coordinates chart grouped by
# the 'wheat_type' feature. Be sure to set the optional
# display parameter alpha to 0.4

plt.figure()
parallel_coordinates(df, 'wheat_type')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import andrews_curves
import matplotlib

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')



# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'

df = pd.read_csv('wheat.data')

# TODO: Drop the 'id' feature, if you included it as a feature


df.drop(df.columns[[0]], axis=1, inplace=True)

plt.figure()
andrews_curves(df, 'wheat_type')
plt.show()
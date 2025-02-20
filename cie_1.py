# -*- coding: utf-8 -*-
"""CIE 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bbXnyr0uvl5S7X0voF3oEHHLpKQh1p8F
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df=pd.read_csv('/content/mtcars.csv')
sns.histplot(df['mpg'],bins=10,color='blue',alpha=0.7)
plt.xlabel('weight')
plt.ylabel('Frequency')
plt.title('Histogram of MPG')
plt.show()



import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df=pd.read_csv('/content/mtcars.csv')
sns.scatterplot(x='wt',y='mpg',data=df)
plt.xlabel('wt')
plt.ylabel('mpg')
plt.title('scatterplot')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df=pd.read_csv('/content/mtcars.csv')
sns.barplot(x='wt',y='mpg',data=df)
plt.xlabel('wt')
plt.ylabel('frequency')
plt.title('barplot of frequency distribution')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df=pd.read_csv('/content/mtcars.csv')
sns.barplot(x='hp',y='mpg',data=df)
plt.xlabel('wt')
plt.ylabel('frequency')
plt.title('boxplot of five number summaries')
plt.show()
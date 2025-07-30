import pandas as pd
import seaborn as and
import matplotlib.pyplot as plt
import numpy as np
df1=pd.read_csv(r'C:\Users\Sunil M S\Downloads\Iris.csv')
df1
 df1.info()
df1.describe()
df.shape
df1.isnull().sum()
df1.drop_duplicates(subset='Species')
df1.value_counts("Species")
sns.countplot(x='Species',data=df1)
sns.scatterplot(x='SepalLengthCm',y='SepalWidthCm',hue='Species',data=df1)
sns.scatterplot(x='SepalLengthCm',y='SepalWidthCm',hue='Species',data=df1)
sns.pairplot(df1.drop(['Id'],axis=1),hue='Species',height=2)
fig,axes=plt.subplots(2,2,figsize=(10,10))
axes[0,0].set_title("Sepal Length")
axes[0,0].hist(df1['SepalLengthCm'],bins=7)
axes[0,1].set_title("Sepal Widthth")
axes[0,1].hist(df1['SepalWidthCm'],bins=7)
axes[1,0].set_title("Petal Length")
axes[1,0].hist(df1['PetalLengthCm'],bins=7)
axes[1,1].set_title("Petal Width")
axes[1,1].hist(df1['PetalWidthCm'],bins=7)
sns.heatmap(df1.select_dtypes(include=['number']).corr(method='pearson').drop(['Id'],axis=1).drop(['Id'],axis=0),annot=True)
plt.show()

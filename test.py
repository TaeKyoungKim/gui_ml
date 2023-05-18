import pandas as pd
from sklearn.preprocessing import LabelEncoder
df= pd.read_csv('../datasets/titanic_train.csv')
# print(df.info())
# cat_col=[x for x in df.columns if df[x].dtype=='object']
# print(cat_col)
# print(df['temp'].isnull().values.any())
print(df['Cabin'])
data = LabelEncoder().fit_transform(df['Cabin'])
print(data)
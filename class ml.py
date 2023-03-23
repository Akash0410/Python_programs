import pandas as pd
df=pd.read_csv('C:\\Users\\Akash Raj\\Downloads\Salary_Data.csv')
print(df.head(5))
import matplotlib.pyplot as plt
plt.scatter(x=df['YearsExperience'],y=df['Salary'])
plt.show()
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
print(lm)
x=df[['YearsExperience']]
y=df['Salary']
lm.fit(x,y)
T = [[2]]
Yhat=lm.predict(T)
Yhat
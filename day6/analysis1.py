#data analysis for height (y) and weight (x)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("linear_simple.csv")
print(df.head())
x_bar = df[["x"]].mean().to_list()
print("The mean of x ", x_bar)
y_bar = df[["y"]].mean().to_list()
print("The mean of y ", y_bar)
df["nr"] = (df['x']-x_bar)*(df['y']-y_bar)
df["dr"] = (df['x']-x_bar)**2
print(df)
nr_sum = df['nr'].sum()
print(nr_sum)
dr_sum = df['dr'].sum()
print(dr_sum)
b_intercept = nr_sum/dr_sum
print(b_intercept)
y_bar = y_bar[0]
x_bar = x_bar[0]
a_intercept = y_bar - b_intercept*x_bar
print(a_intercept)
print("The intercepts of a and b are ", a_intercept, b_intercept)
print ("The equation is  y = ", a_intercept, "+", b_intercept,"x")
a = a_intercept
b = b_intercept
df['y_cap'] = a+b*df['x']
print(df)

#graph
df.plot(kind = 'scatter',x="x",y="y")
x = df['x']
y_cap = df['y_cap']
plt.plot(x,y_cap, color="red", linewidth=3, label = 'y_cap')
plt.show()
plt.savefig("linear_regression.png")

#prediction
#predict the height given  weight is 68
x = 68
pred_y = a+b*x
print(pred_y)
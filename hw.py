import pandas as pd
import matplotlib.pyplot as plt

pd = pd.read_csv("titanic.csv")

gender = pd['Sex'].value_counts()

plt.bar(gender.index,gender.values,color=['blue', 'pink'])
plt.title("Total number of men and women in the Titanic")
plt.xlabel("Gender")
plt.ylabel("Amount")
plt.show()

avg_fare = pd.groupby('Sex')['Fare'].mean()

plt.bar(avg_fare.index,avg_fare.values,color=['pink', 'blue'])
plt.title("Average fare of men and women")
plt.xlabel("Gender")
plt.ylabel("Average Fare")
plt.show()


class_counts = pd['Pclass'].value_counts().sort_values()
names = ['1st Class', '2nd Class', '3rd Class']
colors = ['blue', 'red', 'green']

plt.pie(class_counts.values, labels=names, colors=colors, startangle=90, shadow=True)
plt.title("Passenger Class Distribution")
plt.show()

#Section 7: VISUALISATION


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Titanic_Desaster/train.csv', sep = ',')

titanic = pd.DataFrame(df)

titanic = titanic.set_index('PassengerId')

male_female = pd.value_counts(titanic['Sex'])
plt.pie(male_female)
plt.legend(title='Male: blue, Female: orange')
plt.show()

print(male_female)
new_pie_chart = np.array([577, 314])
mylabels = ["Male", "Female"]
plt.pie(new_pie_chart, labels= mylabels)
plt.show()

# #print(titanic.pivot_table('Fare', 'Age', 'Sex'))
clrz = {'male' : 'navy', 'female' : 'pink'}
titanic_scatter = titanic.plot.scatter(x='Age', y='Fare', c=titanic['Sex'].map(clrz), s = 10)
plt.xlabel('Age (Years)')
plt.ylabel('Fare (Shmeckels)')
plt.legend(title='Male color: navy, Female color: pink')
plt.show()

print(titanic.Survived.value_counts())

plt.xlabel('binned passengers')
plt.ylabel('Fare (Shmeckels)')
plt.hist(titanic['Fare'], bins=30)
plt.show()


new_titanic = titanic.dropna()
print(new_titanic)
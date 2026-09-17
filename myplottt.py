#import matplotlib.pyplot as plt
#plt.plot([1,2,3,4,5],[3,5,7,9,10])
#plt.show()



import matplotlib.pyplot as plt
import pandas as pd

# Sample Data
data = {
    'Name': ['Subhan', 'Ali', 'Hamza', 'Usman', 'Sara'],
    'Department': ['Data Science', 'IT', 'Data Science', 'HR', 'IT'],
    'Salary': [85000, 60000, 95000, 45000, 65000],
    'Experience_Yrs': [2, 4, 5, 1, 3]
}

df = pd.DataFrame(data)
print(df)

plt.bar(df['Experience_Yrs'],df['Salary'],color='teal')
plt.title('Experience vs Salary')
plt.xlabel('Experience_Yrs')
plt.ylabel('Salary')
plt.grid(True)
plt.show()

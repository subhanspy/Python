import pandas as pd
#df = pd.DataFrame({"Name":["Subhan"],"Age":[19]})
#print(df)


df = pd.DataFrame()
df['color'] = ['blue','red','yellow','green']
df['radius'] = [2,4,3,5]
#add diameter column by * 2
df['Diameter']=df['radius']*2
print(df)

print(df['radius'].max())
print(df['Diameter'].sum())
print(df['Diameter'].mean())


# iloc and loc
import pandas as pd

# Sample Employees Data
data = {
    'Name': ['Subhan', 'Ali', 'Hamza', 'Usman', 'Sara'],
    'Department': ['Data Science', 'IT', 'Data Science', 'HR', 'IT'],
    'Salary': [85000, 60000, 90000, 50000, 65000],
    'Experience_Yrs': [2, 4, 5, 1, 3]
}

# Custom Index Set Kar Rahe Hain (Employee IDs)
df = pd.DataFrame(data,index=['EMP101', 'EMP102', 'EMP103', 'EMP104', 'EMP105'])
print("--- ORIGINAL DATAFRAME ---")
print(df)

loc_1=df.loc['EMP105',['Experience_Yrs']]
print(loc_1)
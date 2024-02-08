import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv('Salaries.csv')
print('Basic Data Exploration')
#get the number of rows and columns 
num_rows, num_cols = df.shape
print('number of rows',num_rows,end='')
print()
print('number columns',num_cols,end='')
print()
#determine the data types of each column
print('data types of each column')
print(df.dtypes)
# number of missing values in each column
print('number of missing values in each column',df.isnull().sum(),end='')
print()
print('Descriptive Statistics')
#basic statistics mean, median, mode, minimum, and maximum salary, determine the range of salaries, and find the standard deviation.
max_salary = df['TotalPay'].max()
min_salary = df['TotalPay'].min()
mean_salary = df['TotalPay'].mean()
median_salary = df['TotalPay'].median()
mode_salary = df['TotalPay'].mode()[0]
salary_range = max_salary - min_salary
salary_std = df['TotalPay'].std()
print('max salary',max_salary,end='')
print()
print('min salary',min_salary,end='')
print()
print('mean salary',mean_salary,end='')
print()
print('median salary',median_salary,end='')
print()
print('mode salary',mode_salary,end='')
print()
print('range of salary',salary_range,end='')
print()
print('standard deviation',salary_std,end='')
print()
print('*Data Cleaning*')
#handle data
#first i will fill the missing data in  Status and Notes columns with  0  because 
# the entire 2  columns are  miss filling that is mean  The person who filled  the data does not want to fill  these two columns 
missing_values = df['Notes'].isnull().sum()
if missing_values:
    df['Notes'].fillna(0, inplace=True)
    df.to_csv('Salaries.csv', index=False)
missing_values = df['Status'].isnull().sum()
if missing_values:
    df['Status'].fillna(0, inplace=True)
    df.to_csv('Salaries.csv', index=False)
#second i will fill the missing data in  Benefits column with  0  because 
#Benefits  are not available to all employees
missing_values = df['Benefits'].isnull().sum()
if missing_values:
    df['Benefits'].fillna(0, inplace=True)
    df.to_csv('Salaries.csv', index=False)
#third i will ask the person who fill data to dataset to enter the base salary  that i will fill the missing values in Base pay column 
#because the sal column is between the most important column in dataset 
missing_values = df['BasePay'].isnull().sum()
if missing_values:
    num=input("enter the number to fill missing values in Base Pay column")
    df['BasePay'].fillna(num, inplace=True)
    df.to_csv('Salaries.csv', index=False)
print('Basic Data Visualization')

#histograms  of TotalPay column
plt.hist(df['TotalPay'], bins=40)
plt.xlabel('TotalPay')
plt.ylabel('number of employee that have the same salary')
plt.title('Distribution of Salary')
plt.show()
# pie charts that represent the proportion of employees in different departments.
df[['job', 'Depart']] = df['JobTitle'].str.split('(', expand=True)
df['Depart'] = df['Depart'].str[:-1]
df.to_csv('Salaries.csv', index=False)
df['Depart'].value_counts().plot.pie(labels=df['Depart'].unique())
plt.title('Proportion of Employees in Different Departments')
plt.show()
#Grouped Analysis
#group by year and agency
print('Grouped Analysis')
gSalByYAmean = df.groupby(['Year', 'Agency'])['TotalPay'].mean()
print('mean of salary in group by year and agency',gSalByYAmean,end='')
print()
gSalByYAmax = df.groupby(['Year', 'Agency'])['TotalPay'].max()
print('max of salary in group by year and agency',gSalByYAmax,end='')
print()
gSalByYAmin = df.groupby(['Year', 'Agency'])['TotalPay'].min()
print('min of salary in group by year and agency',gSalByYAmin,end='')
print()
gSalByYAmedian = df.groupby(['Year', 'Agency'])['TotalPay'].median()
print('median of salary in group by year and agency',gSalByYAmedian,end='')
print()
gSalByYAmode = df.groupby(['Year'])['TotalPay'].apply(lambda x: x.mode().iloc[0])
print('mode of salary in group by year and agency',gSalByYAmode,end='')
print()
gSalByYAstd = df.groupby(['Year', 'Agency'])['TotalPay'].std()
print('standard deviation of salary in group by year and agency',gSalByYAstd,end='')
print()
#group by year 
gSalByYmean= df.groupby(['Year'])['TotalPay'].mean()
print('mean of salary in group by year ',gSalByYmean,end='')
print()
gSalByYmax= df.groupby(['Year'])['TotalPay'].max()
print('max of salary in group by year ',gSalByYmax,end='')
print()
gSalByYmin= df.groupby(['Year'])['TotalPay'].min()
print('min of salary in group by year ',gSalByYmin,end='')
print()
gSalByYmedian= df.groupby(['Year'])['TotalPay'].median()
print('median of salary in group by year ',gSalByYmedian,end='')
print()
gSalByYmode = df.groupby(['Year'])['TotalPay'].apply(lambda x: x.mode().iloc[0])
print('mode of salary in group by year ',gSalByYmode,end='')
print()
gSalByYstd= df.groupby(['Year'])['TotalPay'].std()
print('standard deviation of salary in group by year ',gSalByYstd,end='')
print()
#cmpare

print('mean of salary in group by year',gSalByYmean,end='')
print()
print('mean of salary in group by agenct and year',gSalByYAmean,end='')
print()
print('the same')
#correlation
correlation = df['TotalPay'].corr(df['BasePay'])
print(correlation)

df.plot.scatter(x='BasePay', y='TotalPay')
plt.show()


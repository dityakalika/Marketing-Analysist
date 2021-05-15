# Load Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
sns.set_context('notebook')
sns.set_style('whitegrid')
sns.set_palette('Blues_r')

# turn off warnings for final notebook
import warnings
warnings.filterwarnings('ignore')

# load dataset
df = pd.read_csv(r'C:\Users\Ditya Kalika\Documents\Data Analyst\Data Project\Marketing Analyst\marketing_data (Raw Data).csv')
print(df.info())
df.head()

# Clean up column names
# Transform selected columns to numeric format: - Income to float

# Clean up column names that contain whitespace
df.columns = df.columns.str.replace(' ', '')

# Transform Income column to a numerical
df['Income'] = df['Income'].str.replace('$', '')
df['Income'] = df['Income'].str.replace(',', '').astype('float')

# The cleaned dataset:
print(df.head())

# Section 01: Exploratory Data Analysis
# Are there any null values or outliers? How will you wrangle/handle them?

# Null Values
# Identify features containing null values:

df.isnull().sum().sort_values(ascending=False)
#The feature Income contains 24 null values
#Plot this feature to identify best strategy for imputation
#Findings:
#Most incomes are distributed between $0-\$100,000, with a few outliers
#Will impute null values with median value, to avoid effects of outliers on imputation value

plt.figure(figsize=(8,4))
sns.distplot(df['Income'], kde=False, hist=True)
plt.title('Income distribution', size=16)
plt.ylabel('count');

df['Income'].plot(kind='box', figsize=(3,4), patch_artist=True)

# Impute null values in Income, using median value (to avoid skewing of the mean due to outliers):
df['Income'] = df['Income'].fillna(df['Income'].median())
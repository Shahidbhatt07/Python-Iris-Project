import pandas as pd
link = "https://raw.githubusercontent.com/Shahidbhatt07/Python-Iris-Project/refs/heads/main/Iris.csv"
df = pd.read_csv(link)

print("DataSet: \n", df)

# Reading first 5 rows
print("First five rows:", df.head())  # Without passing an argument i.e, 5, by default you will get first 5 rows

# Reading first 7 rows
print("First Seven rows:", df.head(7))

# Reading Last 7 rows
print("Last Seven rows:", df.tail(7))

print("Size of the dataframe = ",df.size) # 150 * 6
print("Shape of the dataframe = ",df.shape)

print("Different columns and their data types: \n", df.info())


# Qualitative data -> represented as Numerical Values - Int, float, Complex
# Quantitative data -> represented as Object - String, boolean, date, list, tuple
# Statistics can be only done on Numerical values

print("Key statistics are \n", df.describe())   #No species there because species is an object
print("Count the missing values \n", df.isnull().sum())
print("Dropping Duplicates:\n", df.drop_duplicates())
print("Shape of dataframe after duplicates are removed: ", df.shape)

# Want to remove duplicates from a particular column
df1= df.drop_duplicates(subset="Species")
print("Shape of dataset after Dropping Duplicates from Species Column:\n", df1.shape)  #(3, 6)

# Balanced dataset: we are analyzing Iris flowers data with 3 species.
# Balanced means all three species should have almost equal number of rows, otherwise
print("Checking Balanced dataset: \n", df.value_counts("Species"))


#Visualization
import matplotlib.pyplot as plt
import seaborn as sns
sns.countplot(data = df, x="SepalLengthCm")
plt.title("No.of rows in Sepal Length")
plt.show()

#Checing Correlation
sns.scatterplot(data=df,x="SepalLengthCm",y="PetalLengthCm")
plt.title("SepalLengthCm v PetalLengthCm")
plt.show()

# multiple plot (2,2) on a single canva(Screen)
fig, axes=plt.subplots(2,2, figsize=(10,10))
axes[0,0].hist(df["SepalLengthCm"], bins = 12)
axes[0,0].set_title(("SepalLengthCm"))
axes[0,1].hist(df["PetalLengthCm"], bins = 12)
axes[0,1].set_title(("PetalLengthCm"))
axes[1,0].hist(df["SepalWidthCm"], bins = 12)
axes[1,0].set_title(("SepalWidthCm"))
axes[1,1].hist(df["PetalWidthCm"], bins = 12)
axes[1,1].set_title(("PetalWidthCm"))
plt.show()


# Boxplot
sns.boxplot(data = df, x ="Species", y="SepalLengthCm")
plt.title("Species vs SepalLengthCm")
plt.show()

#segregate into numeric and non-numeric
import numpy as np
df_num = df.select_dtypes(include=[np.number])
print("Numeric data types: \n",df_num)

df_nonnum = df.select_dtypes(exclude=[np.number])
print("Non Numeric data types: \n",df_nonnum)

print("Mean: \n",df_num.mean())
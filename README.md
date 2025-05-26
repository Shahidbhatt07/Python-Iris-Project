🌸 Iris Dataset Analysis with Python

This project involves performing exploratory data analysis (EDA) and basic visualization on the famous Iris dataset using Pandas, Matplotlib, and Seaborn. The goal is to understand the data structure, identify trends or patterns, check for missing/duplicate values, and visualize relationships between features.

📁 Dataset Source
The Iris dataset used in this project is publicly available and can be accessed from:
https://raw.githubusercontent.com/Shahidbhatt07/Python-Iris-Project/refs/heads/main/Iris.csv

📌 Objectives
Load and inspect the Iris dataset.

Perform basic data exploration (head, tail, shape, info, describe).

Check for missing and duplicate values.

Analyze class balance among species.

Visualize feature distributions and correlations.

Identify numeric vs. non-numeric features.

🧰 Libraries Used
pandas for data manipulation

matplotlib.pyplot and seaborn for data visualization

numpy for handling numeric data types

🔍 Key Explorations
Dataset preview using head(), tail(), and info().

Dataset shape and size.

Summary statistics using describe().

Count of missing values using isnull().sum().

Duplicate removal and validation.

Class balance check with value_counts().

📊 Visualizations
Count plot of Sepal Length

Scatter plot: Sepal Length vs Petal Length

Histograms for all numeric features

Boxplot: Sepal Length vs Species

📑 Code Structure
The code is organized sequentially:

Loading data

Exploratory analysis

Handling duplicates

Visualizations

Data segregation based on type

📈 Output Insights
The dataset is balanced across three species.

No missing values were found.

Clear correlations exist between Sepal and Petal dimensions.

Boxplots reveal feature distribution across species.

✅ Requirements
Make sure the following libraries are installed:
pip install pandas matplotlib seaborn numpy

📬 Feedback
Feel free to fork the project or raise an issue if you have any suggestions or improvements!


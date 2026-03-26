# Netflix Data Analysis Project
# Author: Your Name

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Loading dataset...")

# Step 1: Load dataset
df = pd.read_csv("netflix_titles.csv")

print("Dataset Loaded Successfully")
print(df.head())

# -----------------------------------------
# Step 2: Data Cleaning
# -----------------------------------------

# Remove rows with missing important values
df.dropna(subset=['country','rating','date_added'], inplace=True)

# Remove extra spaces in date column (IMPORTANT FIX)
df['date_added'] = df['date_added'].str.strip()

# Convert to datetime safely
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Extract year added
df['year_added'] = df['date_added'].dt.year

print("Data Cleaning Completed")

# -----------------------------------------
# Analysis 1: Movies added per year
# -----------------------------------------
movies_per_year = df[df['type'] == 'Movie']['year_added'].value_counts().sort_index()

plt.figure(figsize=(10,5))
movies_per_year.plot(kind='line', marker='o')
plt.title("Movies Added Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.grid()
plt.show()

# -----------------------------------------
# Analysis 2: Top Genres
# -----------------------------------------
genre_data = df['listed_in'].str.split(',', expand=True).stack()
top_genres = genre_data.value_counts().head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_genres.values, y=top_genres.index)
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.show()

# -----------------------------------------
# Analysis 3: Top Countries
# -----------------------------------------
country_data = df['country'].str.split(',', expand=True).stack()
top_countries = country_data.value_counts().head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title("Top Countries Producing Netflix Content")
plt.xlabel("Count")
plt.ylabel("Country")
plt.show()

print("🎉 Analysis Completed Successfully!")

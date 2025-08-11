import pandas as pd
#import numpy as np

# #Get a list of floats using python - only highs and lows
# with open("./pittsburgh-weather-2024.csv","r") as file:
#     lines = file.readlines()[1:]  # Skip header
#     data = [list(map(float, line.strip().split(',')[1:3])) for line in lines]  # Only first 2 columns after month

# #Pandas
# df = pd.read_csv("./pittsburgh-weather-2024.csv")

# # Using df.describe() to get mean
# print("\nMean from describe():")
# print(df.iloc[:, 1:3].describe().loc['mean'])

# # Using df.mean() to get mean
# print("\nMean from df.mean():")
# print(df.iloc[:, 1:3].mean())

# # Calculate averages and print in one line
# averages = df.iloc[:, 1:3].mean()
# print("Pandas averages:")
# print(averages.to_string(float_format='{:.2f}'.format))

# #Numpy
# print("NumPy averages with pandas:")
# print(np.mean(df.iloc[:, 1:3].values, axis=0))

# #Numpy averages with python - highs and lows only
# print("NumPy averages (highs and lows):")
# print(np.mean(data, axis=0))  # axis=0 for column averages

df = pd.read_csv("/Users/david/Documents/GitHub/Ai2C/AI2C-Prereqs/lesson09/pandas/all_olympic_medalists.csv")

#1. First five last five rows
# print("First five rows:")
# print(df.head())
# print("\nLast five rows:")
# print(df.tail())

# #2. How many rows
# print("Rows", len(df))

# #3. Is there an empty coloumn
# print(df.isna().all().all())

# #4 Total medals
# print(df['medal'].count())

# #5
 
# #6 How many medals by the US
print(df[df['country'] == 'United States']['medal'].count())

#Exercise 3
# df = pd.read_csv("/Users/david/Documents/GitHub/Ai2C/AI2C-Prereqs/lesson09/pandas/top-20-womens-tours.csv")

# rank = df["Rank"]
# peak = df["Peak"]
# artist = df["Artist"]
# tour = df["Tour title"]

# #Shows rows and coloumns
# print(df["Artist"].shape)

# print(df["Artist","Peak"].shape)
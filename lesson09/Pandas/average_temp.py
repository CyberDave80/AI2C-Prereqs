import csv

with open('pittsburgh-weather-2024.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    daily_highs = []
    daily_lows = []
    for row in reader:   
        daily_highs.append(row[1])
        daily_lows.append(row[2])

#print(daily_highs)

sum_highs = 0
for temp in daily_highs[1:]:
    sum_highs += float(temp)

sum_lows = 0
for temp in daily_lows[1:]:
    sum_lows += float(temp)

average_high = sum_highs/(len(daily_highs) - 1)

average_lows = sum_lows/(len(daily_lows)-1)

print("The average daily high was",round(average_high,2))
print("The average daily low was", average_lows)
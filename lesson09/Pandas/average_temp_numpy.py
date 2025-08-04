import numpy

with open('pittsburgh-weather-2024.csv','r') as file:
    daily = []
    for row in file:
        daily.append(row.strip().split(","))

daily_highs = []
for day in daily[1:]:
    daily_highs.append(float(day[1]))

average = numpy.mean(daily_highs)

print(f"{average:.2f}")
import csv

with open("./pittsburgh-weather-2024.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)[1:]  # Skip month column in header
    
    # Collect values by column
    columns = [[] for _ in header]
    
    for row in reader:
        for i, val in enumerate(row[1:]):  # Skip month column
            if val.replace('.', '').replace('-', '').isdigit():
                columns[i].append(float(val))
    
    # Calculate average for each column
    for i, col_name in enumerate(header):
        if columns[i]:
            avg = sum(columns[i]) / len(columns[i])
            print(f"{col_name} average: {avg:.2f}")
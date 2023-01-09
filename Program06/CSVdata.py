# Kristi LaVigne
# CSCI 236
# 03/27/2020
# Program 06 - Pandas
# hours: 5
# Grade Version - n/a
# major problems: errors, doesn't find the heading 'cylinders'
# status of the program - doesn't compile
# ---------------------------------------------------------------------------------------------------------------
import pandas as panda

csv_file = panda.read_csv("vehicles.csv")  # Read file to pandas dataframe

# Question 1:
# ------------
# Finding rows with 6-cylinder vehicles
six_cylinders = csv_file[csv_file['cylinders'] == '6 cylinders']
# Removing zero/null values
odometers = six_cylinders['odometer'].dropna()
# Calculating average odometer reading
avg_odometer = odometers.sum() / len(odometers)
# Displaying the result
print(f"Average Odometer Reading for 6 cylinder vehicles: {round(avg_odometer, 2)}")

# Question 2:
# ------------
# Finding the rows containing SUV
suv = csv_file[csv_file['type'] == 'SUV']
# Removing zero/null values
suv_price = suv['price'].dropna()
# Calculating the average SUV price
avg_suv_price = suv_price.sum() / len(suv_price)
# Displaying the result
print(f"Average price of SUVs: {round(avg_suv_price, 2)}")

# Question 3:
# ------------
# Finding the rows containing pickup-trucks
trucks = csv_file[(csv_file['type'] == 'pickup') | (csv_file['type'] == 'truck')]
# Removing zero/null values
truck_price = trucks['price'].dropna()
# Calculating the average truck price
avg_truck_price = truck_price.sum() / len(truck_price)
# Displaying the result
print(f"Average price of pickup-trucks: {round(avg_truck_price, 2)}")  # Print result

# Question 4:
# ------------
# Initializing the dictionary
fuel_dict = {}
# Iterating through unique fuel type
for k in csv_file['fuel'].unique():
    # Initializing the dictionary
    dict_unique = {}
    # Removing zero/null values
    df_fuel = csv_file.loc[csv_file['fuel'] == k, 'manufacturer'].dropna()
    # Iterating trough the data
    for i in df_fuel:
        # Checking to see if the key is already in the dictionary
        if i in dict_unique:
            dict_unique[i] += 1
        # Adding the key value pair if it isn't in the dictionary
        else:
            dict_unique[i] = 1
    # Sorting the dictionary alphabetically
    dict_unique = sorted(dict_unique.items())
    # Checking to see if the key is already in the dictionary
    if k in fuel_dict:
        fuel_dict[k] = fuel_dict[k] + dict_unique
    # Adding the key value pair if it isn't in the dictionary
    else:
        fuel_dict[k] = dict_unique
# Displaying the resulting dictionary
print(fuel_dict)

# CHALLENGE PROBLEMS
# YOU MAY NOT USE ANY ADDITIONAL LIBRARIES OR PACKAGES TO COMPLETE THIS CHALLENGE

Name: Yihao Li

# Divvy is Chicago's bike share system, which consists of almost 600 stations scattered
# around the city with blue bikes available for anyone to rent. Users begin a ride by removing
# a bike from a dock, and then they can end their ride by returning the bike to a dock at any Divvy 
# station in the city. You are going to use real data from Divvy collected at 1:30pm on 4/7/2020 
# to analyze supply and demand for bikes in the system. 

# NOTE ** if you aren't able to run this, type "pip install json" into your command line
import json

# do not delete; this is the data you'll be working with
divvy_stations = json.loads(open('/Users/YIHAOLI/Desktop/divvy_stations.txt').read())

# PROBLEM 1
# find average number of empty docks (num_docks_available) and 
# available bikes (num_bikes_available) at all stations in the system

bikes_available = []
docks_available = []

for item in divvy_stations:
    docks_available.append(item['num_docks_available'])
    bikes_available.append(item["num_bikes_available"])

average_number_of_empty_bikes = sum(bikes_available) / len(bikes_available)
average_number_of_empty_docks = sum(docks_available) / len(docks_available)
average_number_of_empty_bikes 
average_number_of_empty_docks

# PROBLEM 2
# find ratio of bikes that are currently rented to total bikes in the system (ignore ebikes)

bikes_rented = []
bikes_available = []

for item in divvy_stations:
    bikes_rented.append(item["num_docks_available"])
    bikes_available.append(item["num_bikes_available"])
total_rented_bikes = sum(bikes_rented)
total_available_bikes = sum(bikes_available)

total_bikes = total_available_bikes + total_rented_bikes
ratio = total_rented_bikes/total_bikes
ratio  

# PROBLEM 3 
# Add a new variable for each divvy station's entry, "percent_bikes_remaining", that shows 
# the percentage of bikes available at each individual station (again ignore ebikes). 
# This variable should be formatted as a percentage rounded to 2 decimal places, e.g. 66.67%

for item in divvy_stations:
    item.update({"percent_bikes_remaining" : item["num_bikes_available"]/ (item["num_bikes_available"] + item["num_docks_available"])})
    item["percent_bikes_remaining"] = str(round(item["percent_bikes_remaining"] * 100, 2)) + "%"


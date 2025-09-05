# city_reader.py
# Read the city data from a CSV File
# Starter Code from CSC 210
# Modified by: [Jackie Arteaga]

from csv import DictReader
from city_data import CityData

def read_city_from_csv(file_path, city_name):
    with open(file_path, 'r') as file:
        reader = DictReader(file, delimiter='t') # used chatgpt to help for 't' to handle tab-separated data
        years = []
        populations = []

        for row in reader:
            if row ['City'] == city_name:
                year = int(row['Year']) # help from Google AI to figure out hwo to convert string to integer
                pop = int(row['Population'])
                years.append(year)
                populations.append)pop)

        start_year = min(years)
        end_year = max(years)
        return CityData(city_name, start_year, end_year, populations)

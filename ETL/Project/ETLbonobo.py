# IMPORT LIBRARIES
import glob
import csv
import os.path
import xml.etree.ElementTree as ET
import zipfile as z
# from collections import namedtuple
from datetime import datetime

import bonobo
import requests

# create a bonobo graph for the data
extract_data = bonobo.Graph()
transformed_data = bonobo.Graph()

dataGraph = bonobo.Graph() #used in extract from csv

 # create a dictionary to hold extracted data
extracted_data = {}

# CSV EXTRACT FUNCTION / also WRITES CSV
def extract_from_csv(file_to_process, _limit:None, _print=False):

    trunk = dataGraph.add_chain(bonobo.CsvReader(file_to_process), *((bonobo.Limit(_limit),) if _limit else ()) )
    
    if _print:
        dataGraph.add_chain(bonobo.PrettyPrinter(), _input=trunk.output)

    dataGraph.add_chain(bonobo.CsvWriter( "data/extracted/*.csv", fs="fs.output" ), _input=trunk.output)

    return extracted_data


# JSON EXTRACT FUNCTION
def extract_from_json(file_to_process, _limit=None, _print=False):

    graph = bonobo.Graph()

    trunk = graph.add_chain(
        bonobo.JsonReader(file_to_process), *((bonobo.Limit(_limit),) if _limit else ()) )

    if _print:
        graph.add_chain(bonobo.PrettyPrinter(), _input=trunk.output)

    graph.add_chain(bonobo.JsonWriter("data/extracted/*.json", fs="fs.output"), _input=trunk.output)
    graph.add_chain(bonobo.LdjsonWriter("data/extracted/*.json", fs="fs.output"), _input=trunk.output)

    return graph


def extract():               
    #process all csv files
    for csvfile in glob.glob("data/extracted/*.csv"):
        dataGraph = extract_from_csv(csvfile,None)
        
    # process all json files
    for jsonfile in glob.glob("data/extracted/*.json"):
        extract_from_json(jsonfile,None)

    return dataGraph

# TRANSFORM
def transform(data):
    data_to_transform = {}
    # convert into dictionary
    # using dict method
    for each in data_to_transform:
       data_to_transform = dict(each._asdict())

    # Iterate through the named tuple and convert the height and weight
    for row in data:
        # Convert height which is in inches to millimeter
        # Convert the datatype of the column into float
        # Convert inches to meters and round off to two decimals(one inch is 0.0254 meters)
        data_to_transform['height'] = round(each * 0.0254,2)
        # yield row._replace(height=round(row.height * 0.0254,2))

        # Convert weight which is in pounds to kilograms
        # Convert the datatype of the column into float
        # Convert pounds to kilograms and round off to two decimals(one pound is 0.45359237 kilograms)
        data_to_transform['weight'] = round(each * 0.45359237,2 )
        # yield row._replace(weight=round(row.weight * 0.45359237,2))

    return data

# LOADING
def load(targetfile, data_to_load):
    data_to_write = {}
    # convert into dictionary
    # using dict method
    for i in data_to_load:
       data_to_write = dict(i._asdict())

    with open(targetfile, 'w') as csvfile:
        writer = csv.DictWriter(csvfile,  ['name','height','weight'])
        writer.writeheader()
        writer.writerows(data_to_write)


# LOGGING
def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S:%f' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.utcnow() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("data/ETL/logfile_b.txt","a") as f:
        f.write(timestamp + ',' + message + '\n')


# DOWNLOAD THE FILE
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip'
r = requests.get(url, allow_redirects=True)
print(r.headers.get('content-type'))


# SAVE THE ZIP FILE
save_path = 'data/raw/'
file_name = "../source.zip"
complete_name = os.path.join(save_path, file_name)

open(complete_name, "wb").write(r.content)


# UNZIP THE FILE
root = z.ZipFile(complete_name)
root.extractall('data/extracted/')
root.close()

# SET PATHS
tmpfile = "temp.tmp"               # file used to store all extracted data
logfile = "logfile_b.txt"            # all event logs will be stored in this file
targetfile = "data/ETL/transformed_data_b.csv"   # file where transformed data is stored

# running the ETL 10 times
for i in range(10):
    log('run: '+ str(i))

    # LOGGING EACH STAGE AND SIGNALLING START/END
    log("ETL Job Started")
    log("Extract phase Started")
    extract_data = extract()
    log("Extract phase Ended")
    extract_data

    log("Transform phase Started")
    transformed_data = transform(extract_data)
    log("Transform phase Ended")
    transformed_data

    log("Load phase Started")
    load(targetfile, transformed_data)
    log("Load phase Ended")

    log("ETL Job Ended")
    log("------------------------------")


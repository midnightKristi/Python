# ---
# title: "Web scraping with Python"
# always_allow_html: yes
# output:
#   html_document:
#     highlight: tango
#     toc: true
#     toc_float:
#       collapsed: true
# jupyter:
#   jupytext_format_version: '1.3'
#   jupytext_formats: ipynb,Rmd:rmarkdown,py:light,md:markdown
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.7.0
#   name: PythonWebScrape.ipynb
#   toc:
#     base_numbering: '1'
#     nav_menu:
#       height: 542px
#       width: 461px
#     number_sections: true
#     sideBar: true
#     skip_h1_title: true
#     title_cell: Table of Contents
#     title_sidebar: Contents
#     toc_cell: false
#     toc_position: null
#     toc_section_display: true
#     toc_window_display: true
# ---

# <style type="text/css">
# pre code {
#     display: block;
#     unicode-bidi: embed;
#     font-family: monospace;
#     white-space: pre;
#     max-height: 400px;
#     overflow-x: scroll;
#     overflow-y: scroll;
#     }
# </style>

# + {"hide_input": true, "results": "'hide'"}
# This part is optional; it sets some printing options that make output look nicer.


from pprint import pprint as print
import pandas as pd

pd.set_option('display.width', 133)
pd.set_option('display.max_colwidth', 30)
pd.set_option('display.max_columns', 5)

ds_wiki = 'https://dontstarve.fandom.com/wiki/Characters'
collection_path = 'browse'

collection_url = (ds_wiki
                  + "/"
                  + collection_path)

print(collection_url)

# Note that we omit the parameters here because it is usually easier to
# pass them as a `dict` when using the `requests` library in Python.
#
# Now that we've constructed the URL we wish interact with we're ready
# to make our first request in Python.

import requests

collections1 = requests.get(
    collection_url,
    parameters={'load_amount': 10,
                'offset': 0}
)
# -

# ### Parsing JSON data
collections1.headers['Content-Type']

# Since JSON is a structured data format, parsing it into python data
# structures is easy. In fact, there's a method for that!
collections1 = collections1.json()
print(collections1)

print(collections1.keys())

record_keys = collections1['records'][0].keys()
print(record_keys)

# Next we can specify the fields we are interested in and use a dict
# comprehension to organize the values;

records1 = {k: [record.get(k, 'NA')
                for record in collections1['records']]
            for k in record_keys}

# Finally we can convert the dict to a `DataFrame`

import pandas as pd

records1 = pd.DataFrame.from_dict(records1)

print(records1)

# and write the data to a file.

records1.to_csv("records1.csv")

# Iterating to retrieve all the data
records = [requests.get(collection_url,
                        parameters={'load_amount': 10,
                                    'offset': str(offset)}).json()['records']
           for offset in range(0, 50, 10)]

# For convenience we can flatten the records in each list into one long
# `records` list

records_final = []
for record in records:
    records_final += record

# write the data to a .csv file
records_final = {k: [record.get(k, 'NA')
                     for record in records_final]
                 for k in record_keys}

# convert the dict to a `DataFrame`
records_final = pd.DataFrame.from_dict(records_final)

# write the data to a file.
records_final.to_csv("records_final.csv")

print(records_final)

# Retrieving HTML
calendar_path = 'visit/calendar'

calendar_url = (ds_wiki  # recall that we defined museum_domain earlier
                + "/"
                + calendar_path)

print(calendar_url)

events0 = requests.get(calendar_url, parameters={'date': '2018-11'})

# check the headers to see what type of content was received
events0.headers['Content-Type']

# ### Parsing HTML using the lxml library

from lxml import html

events_html = html.fromstring(events0.text)

# Using xpath to extract content from HTML + {"results": "'hide'"}
html.open_in_browser(events_html, encoding='UTF-8')

# extracting the element of interest:
events_list_html = events_html.xpath('//*[@id="events_list"]')[0]

# the first element in our  list + {"results": "'hide'"}
first_event_html = events_list_html[0]
html.open_in_browser(first_event_html, encoding='UTF-8')

# By repeating this process for each element,
# list of the xpaths to those elements.

elements_we_want = {'figcaption': 'div/figure/div/figcaption',
                    'date': 'div/div/header/time',
                    'title': 'div/div/header/h2/a',
                    'time': 'div/div/div/p[1]/time',
                    'localtion1': 'div/div/div/p[2]/span/span[1]',
                    'location2': 'div/div/div/p[2]/span/span[2]'
                    }

# iterate over the elements we want and extract them.
first_event_values = {key: first_event_html.xpath(
    elements_we_want[key])[0].text_content().strip()
                      for key in elements_we_want.keys()}

print(first_event_values)


# -

# Iterating to retrieve content from a list of HTML elements
# handle the case where one or more of these elements is not available
# a function that tries to retrieve a value and returns an empty string if it fails.

def get_event_info(event, path):
    try:
        info = event.xpath(path)[0].text.strip()
    except:
        info = ''
    return info


# iterate over the list of events and
# extract the available information for each one.
all_event_values = {key: [get_event_info(event, elements_we_want[key])
                          for event in events_list_html]
                    for key in elements_we_want.keys()}

# arrange these values in a pandas `DataFrame`
# and save them as .csv files
all_event_values = pd.DataFrame.from_dict(all_event_values)

all_event_values.to_csv("all_event_values.csv")

print(all_event_values)

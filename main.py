import requests
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd

url = 'https://www.dublincity.ie/residential/parks/dublin-city-parks/pitch-playability'
data = requests.get(url)

my_data = []
html = BeautifulSoup(data.text, 'html.parser')
rows = html.select('tr')

for row in rows[1:]:
    park = row.select('td')[0].get_text()
    status_on = row.select('td')[1].get_text()
    my_data.append({
        "Parks": park,
        "Status": status_on
    })

df = pd.DataFrame(my_data)
df['Status'] =  df['Status'].replace('\xa0', 'OFF')

df.to_csv('data.csv')
"""
f = open('PitchPlayability.txt', 'x')

f.write(df.to_string())

f.close()
"""
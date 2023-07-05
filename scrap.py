import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class': 'wikitable sortable'})

data = []
for row in table.find_all('tr'):
    cols = row.find_all('td')
    if len(cols) > 0:
        rank = cols[0].text.strip()
        name = cols[1].text.strip()
        population_2011 = cols[2].text.strip()
        population_2001 = cols[3].text.strip()
        state_or_union_territory = cols[4].text.strip()
        data.append([rank, name, population_2011, population_2001, state_or_union_territory])

df = pd.DataFrame(data, columns=['Rank', 'Name', 'Population_2011', 'Population_2001', 'State_or_Union_Territory'])
df.to_csv('cities.csv', index=False)

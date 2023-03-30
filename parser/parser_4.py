import requests
from bs4 import BeautifulSoup
import os

# Send a GET request to the web page
url = 'https://www.worldatlas.com/countries'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element containing the country information
table = soup.find('table', {'class': 'content_table'})

if table:
    # Find all the rows in the table
    rows = table.find_all('tr')

    # Loop through each row and extract the country name and ISO alpha-2 code
    iso2_codes = {}
    for row in rows:
        td_tags = row.find_all('td')
        if len(td_tags) >= 2:
            country_name = td_tags[0].text.strip()
            iso2_code = td_tags[1].text.strip()
            iso2_codes[country_name] = iso2_code

            # Rename the corresponding image file
            old_filename = f"{country_name}_{country_name}.jpg"
            new_filename = f"{iso2_code}.jpg"
            os.rename(f"country_logos/{old_filename}", f"country_logos/{new_filename}")
else:
    print("Error: table not found on the page.")

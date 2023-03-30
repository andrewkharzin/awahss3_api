import requests
import os
from bs4 import BeautifulSoup

url = "https://www.worldatlas.com/countries"

# Fetch the HTML content of the page
print(f"Fetching {url}...")
try:
    response = requests.get(url)
    response.raise_for_status()  # raise an exception if there was an HTTP error
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred while fetching {url}: {e}")
    exit()

# Create a folder to store the flag images
folder_name = "country_logos"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Map ISO alpha-2 codes to country names
iso_codes_to_names = {}
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table")
for tr in table.find_all("tr")[1:]:  # skip the first row (header row)
    td_tags = tr.find_all("td")
    if len(td_tags) < 2:  # skip row if it doesn't have at least 2 td elements
        continue
    iso_code = td_tags[0].text.strip()
    country_name = td_tags[1].text.strip()
    iso_codes_to_names[iso_code] = country_name

# Download and save the flag images to the folder
print("Downloading country flags...")
img_tags = soup.find_all("img")
for i, img_tag in enumerate(img_tags):
    try:
        img_url = img_tag["src"]
        # iso_code = img_tag["alt"].split()[-1]  # extract ISO alpha-2 code from alt attribute
        country_name = iso_codes_to_names.get(iso_code, iso_code)  # get country name from mapping, or use code if not found
        response = requests.get(img_url)
        response.raise_for_status()  # raise an exception if there was an HTTP error
    except (requests.exceptions.HTTPError, KeyError) as e:
        print(f"Error occurred while processing image {img_url}: {e}")
        continue  # skip this image and move on to the next one

    with open(os.path.join(folder_name, f"{iso_code}_{country_name}.jpg"), "wb") as f:
     f.write(response.content)

print("Done downloading country flags!")

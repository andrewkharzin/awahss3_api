from requests_html import HTMLSession
import os
import requests
from urllib.parse import urljoin  # Import the urljoin function

# Define the base URL and the URL to scrape
base_url = 'https://www.americasfinestlabels.com/'
url = 'hazardous-material/labels/iata#2'

# Create an HTML session
session = HTMLSession()

# Send an HTTP GET request to the URL
# Use urljoin to create the full URL
response = session.get(urljoin(base_url, url))

# Check if the request was successful
if response.status_code == 200:
    print("Request successful. Parsing data...")

    # Sleep to allow JavaScript to render the page (you can adjust this time)
    response.html.render(sleep=5)

    # Find and extract image URLs and descriptions
    for label_item in response.html.find('td.static.products_image'):
        image_url = urljoin(base_url, label_item.find(
            'img')[0].attrs['data-src'])  # Prepend base_url
        description = label_item.find('img')[0].attrs['alt']

        # Print the image URL and description to check if the parser is working
        print(f"Image URL: {image_url}")
        print(f"Description: {description}")

        # Save the images to the 'shcimg' folder
        image_data = requests.get(image_url).content
        image_name = description + '.jpg'
        with open(os.path.join('shcimg', image_name), 'wb') as img_file:
            img_file.write(image_data)

    print("Images saved to 'shcimg' folder.")
else:
    print(
        f"Failed to retrieve the webpage. Status code: {response.status_code}")

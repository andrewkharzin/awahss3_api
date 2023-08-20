import requests
from bs4 import BeautifulSoup
import os

# Define the URL of the airhex.com airline logos page
url = 'https://www.airhex.com/airlines'

# Send a GET request to the URL and retrieve the HTML response
response = requests.get(url)

# Parse the HTML response using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the airline logos on the page
airline_logos = soup.find_all('img', class_='airline-logo')

# Create a folder to store the downloaded logos
folder_name = 'airline_logos'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Loop through each airline logo
for index, logo in enumerate(airline_logos, 1):
    try:
        # Get the URL of the airline logo image
        image_url = logo['src']
        
        # Send a GET request to download the logo image
        image_response = requests.get(image_url)
        
        # Generate the file name for the downloaded logo image
        file_name = f'airline_logo_{index}.png'
        
        # Save the downloaded logo image to the folder
        with open(os.path.join(folder_name, file_name), 'wb') as file:
            file.write(image_response.content)
        
        # Display console status of completed download
        print(f'Successfully downloaded {file_name}')
        
    except Exception as e:
        # Display console status of error
        print(f'Error downloading airline logo {index}: {str(e)}')
        
print('Logo parsing and downloading completed!')

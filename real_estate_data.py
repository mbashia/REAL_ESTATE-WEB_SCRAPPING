from bs4 import BeautifulSoup
import requests
import openpyxl
from openpyxl import Workbook

# scrapping real estate data from property24.co.ke

real_estate_data = Workbook()
ws = real_estate_data.active
headings = ["price", "location", "no_bedrooms", "no_bathrooms", "no_garages", "house_description"]
ws.append(headings)
url = "https://www.property24.co.ke/property-for-sale-in-nairobi-p95"
response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")
properties = soup.find_all("div", class_="pull-left sc_listingTileContent")
property_data = []
for property in properties:

    try:
        price = property.find("div", class_="sc_listingTilePrice primaryColor").span.text.strip()

    except:
        price = "___"
    print(price)
    property_data.append(price)
    try:
        location = property.find("div", class_='sc_listingTileAddress primaryColor').text.strip()
    except:
        location = "___"
    property_data.append(location)
    try:
        no_bedrooms = property.find_all("span")[1].text
    except:
        no_bedrooms = "___"
    property_data.append(no_bedrooms)
    try:
        no_bathrooms = property.find_all("span")[2].text
    except:
        no_bathrooms = "___"
    property_data.append(no_bathrooms)
    try:
        no_garages = property.find_all("span")[3].text
    except:
        no_garages = "___"
    property_data.append(no_garages)

    house_description = property.find("div", class_="sc_listingTileTeaser").text.strip()
    # property_data.append(house_description)
    print(price)
    print(location)
    print(no_bedrooms)
    print(no_bathrooms)
    print(no_garages)
    print(house_description)
    print("\n")

    ws.append(property_data)
    property_data = []

real_estate_data.save("real_estate_data.xlsx")

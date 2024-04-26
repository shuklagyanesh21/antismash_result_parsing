import os
os.getcwd()
os.chdir("/home/gyanesh/trial/Python")



import csv
from bs4 import BeautifulSoup

# Parse the HTML file
with open('index.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find the table with the region information
table = soup.find('table', class_='cc-heat-table')

# Open the CSV file for writing
with open('regions_info.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

     # Write header row
    writer.writerow(['Region', 'Type', 'Size', 'Split Left', 'Link', 'Description', 'Similarity'])
    
    # Find all table rows in the tbody
    for row in soup.find('tbody').find_all('tr'):
        # Extract data from each row
        cells = row.find_all('td')
        region = cells[0].text.strip()
        type = cells[1].text.strip()
        size = cells[2].text.strip()
        split_left = cells[3].text.strip()
        link = cells[4].text.strip()
        description = cells[5].text.strip()
        similarity = cells[6].text.strip()
        
        # Write row to CSV file
        writer.writerow([region, type, size, split_left, link, description, similarity])

print("CSV file 'regions_info.csv' has been created successfully!")

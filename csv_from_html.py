import os
import csv
from bs4 import BeautifulSoup

# Get the current working directory
current_dir = os.getcwd()
directory_name = os.path.basename(current_dir)

# Load the HTML file
with open('index.html', 'r') as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table elements
tables = soup.find_all('table', class_='region-table')

# Extract the data from the tables
data = []
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 7:
            region = cells[0].text.strip()
            region_type = cells[1].text.strip()
            region_from = cells[2].text.strip()
            region_to = cells[3].text.strip().replace(',', '')
            mibig = cells[4].text.strip()
            mibig_type = cells[5].text.strip()
            similarity = cells[6].text.strip()
            data.append([directory_name, region, region_type, region_from, region_to, mibig, mibig_type, similarity])
        elif len(cells) >= 4:
            region = cells[0].text.strip()
            region_type = cells[1].text.strip()
            region_from = cells[2].text.strip()
            region_to = cells[3].text.strip().replace(',', '')
            data.append([directory_name, region, region_type, region_from, region_to, '', '', ''])

# Write the data to a CSV file
with open('regions_info.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write header row
    #writer.writerow(['Directory', 'Region', 'Type', 'From', 'To', 'Most similar known cluster', 'Similarity'])
    writer.writerows(data)

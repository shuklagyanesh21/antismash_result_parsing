import os
import csv
from bs4 import BeautifulSoup

os.chdir("/home/user/yourpath")

# Parse the HTML file
with open('index.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find the table with the region information
table = soup.find('table', class_='cc-heat-table')

# Open the CSV file for writing
with open('regions_info.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write header row
    writer.writerow(['Region', 'Type', 'From', 'To', 'Most similar known cluster', 'miBiG Type', 'Similarity'])

    # Find all table rows in the tbody
    for row in soup.find('tbody').find_all('tr'):
        # Extract data from each row
        cells = row.find_all('td')
        if len(cells) < 7:
            # Handle the case where the row has fewer than 7 columns
            region = cells[0].text.strip() if len(cells) > 0 else ''
            type = cells[1].text.strip() if len(cells) > 1 else ''
            size = cells[2].text.strip() if len(cells) > 2 else ''
            split_left = cells[3].text.strip() if len(cells) > 3 else ''
            link = cells[4].text.strip() if len(cells) > 4 else ''
            description = cells[5].text.strip() if len(cells) > 5 else ''
            similarity = cells[6].text.strip() if len(cells) > 6 else ''
        else:
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

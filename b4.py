import re
import pandas as pd
from bs4 import BeautifulSoup

# Load the HTML content
with open('ServiceWebSite.txt', 'r') as f:
    html_content = f.read()

# Parse the HTML using Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# Initialize lists to store extracted data
names = []
phones = []
emails = []

# Find all rows in the table
table_rows = soup.find_all('tr')[1:]  # Exclude the header row

# Loop through each row and extract the required information
for row in table_rows:
    columns = row.find_all('td')
    if len(columns) >= 5:
        name = columns[0].text.strip()
        phone = columns[3].text.strip()
        email = columns[4].text.strip()

        names.append(name)
        phones.append(phone)
        emails.append(email)

# Create a DataFrame
data = {'Name': names, 'Phone': phones, 'Email': emails}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
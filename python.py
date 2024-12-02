import requests
from bs4 import BeautifulSoup


def fetch_table_data(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')

    table_data = []
    for row in rows[1:]:
        cells = row.find_all('td')
        if len(cells) >= 3:
            x = int(cells[0].text.strip())
            character = cells[1].text.strip()
            y = int(cells[2].text.strip())
            table_data.append((x, y, character))

    print_chars(table_data)


def print_chars(table_data):
    grid = {}
    for x, y, char in table_data:
        grid[(x, y)] = char

    max_y = max(y for x, y, char in table_data)
    for y in range(max_y + 1):
        row = ""
        for x in range(0, max(x for x, y, char in table_data) + 1):  # Go from 0 to max_x
            row += grid.get((x, y), " ")
        print(row)


url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
fetch_table_data(url)

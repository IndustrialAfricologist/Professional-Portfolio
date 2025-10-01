import csv
import tkinter as tk
from tkinter import filedialog
import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    """Fetch the HTML content of the given URL."""
    try:
        response = requests.get(url, timeout=10)  # Added timeout argument
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

def parse_countries(html):
    """Parse the HTML to extract country data."""
    soup = BeautifulSoup(html, 'html.parser')
    countries_data = []

    # Find all country entries
    countries = soup.find_all('div', class_='country')

    for country in countries:
        # Extract country details
        country_name = country.find('h3', class_='country-name').text.strip()
        capital = country.find('span', class_='country-capital').text.strip()
        population = country.find('span', class_='country-population').text.strip()
        area = country.find('span', class_='country-area').text.strip()

        # Store country information in a dictionary
        country_info = {
            'Country': country_name,
            'Capital': capital,
            'Population': population,
            'Area': area
        }
        countries_data.append(country_info)

    return countries_data

def save_to_csv(data):
    """Save the extracted data to a CSV file chosen by the user."""
    if not data:
        print("No data to save.")
        return

    # Create a Tkinter root window (it won't be shown)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Prompt the user to select a file location and name
    filename = filedialog.asksaveasfilename(
        defaultextension=".csv", 
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
        title="Save as"
    )

    if filename:  # Check if the user selected a file
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

        print(f"Data has been successfully saved to {filename}.")
    else:
        print("Save operation was cancelled.")

def scrape_and_save_countries():
    """Fetch country data from a website, parse it, and save it to a CSV file."""
    url = 'https://www.scrapethissite.com/pages/simple/'
    html = fetch_html(url)
    if html:  # Check if HTML was fetched successfully
        countries_data = parse_countries(html)
        save_to_csv(countries_data)  # Call with only the data argument
        print("Data has been successfully scraped and saved.")
    else:
        print("Failed to retrieve data.")

if __name__ == '__main__':
    scrape_and_save_countries()
# Scrape Smart: Structured HTML Extraction from Scrape This Site with BeautifulSoup

## Project Overview
"Scrape Smart" is a lightweight Python script designed to extract structured educational data from the Scrape This Site sandbox using the `requests` and `BeautifulSoup` libraries. The extracted data is transformed into a clean tabular format and exported as a CSV file. This project serves as a demonstration of ethical web scraping and structured data extraction.

## Code Overview
The code consists of several key functions that work together to scrape and save data:

1. **`fetch_html(url)`**: This function takes a URL as input and uses the `requests` library to fetch the HTML content of the page. It includes a timeout to prevent indefinite hanging and raises an error if the response is not successful, ensuring that only valid HTML is processed.

2. **`parse_countries(html)`**: This function receives the HTML content and uses `BeautifulSoup` to parse it. It searches for all country entries within the HTML structure, extracting relevant information such as the country name, capital, population, and area. The extracted data is stored in a list of dictionaries, where each dictionary represents a country.

3. **`save_to_csv(data)`**: This function prompts the user to select a file location and name for saving the extracted data. It uses the `tkinter` library to create a file dialog for user interaction. The data is then written to a CSV file using the `csv` module, with appropriate headers.

4. **`scrape_and_save_countries()`**: This is the main function that orchestrates the workflow. It defines the target URL, calls the `fetch_html` function to retrieve the HTML content, processes it with `parse_countries`, and finally saves the structured data to a CSV file using `save_to_csv`.

## Output
The script extracts the following data for each country:
- Country Name
- Capital
- Population
- Area

The data is saved as a CSV file chosen by the user.

## Required Libraries
To run this project, you need to install the following libraries:
- `requests`
- `beautifulsoup4`
- `csv` (included with Python standard library)
- `tkinter` (included with Python standard library)

You can install the required libraries using pip:
```bash
pip install requests beautifulsoup4
```

## Usage
To run the script, simply execute it in your Python environment. A file dialog will prompt you to choose a location to save the extracted data as a CSV file.
```
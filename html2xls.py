import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO

try:
    # Reading HTML-file
    with open("your_file.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    # Parsing HTML
    soup = BeautifulSoup(html_content, "html.parser")
    tables = soup.find_all("table")  # Find all sheets

    if not tables:
        raise ValueError("No tables were found in the HTML\file.")

    # Convert first table to  DataFrame
    table_html = str(tables[0])  # Convert table to string
    df = pd.read_html(StringIO(table_html))[0]  # Using StringIO

    # Saving to Excel
    df.to_excel("output.xlsx", index=False)
    print("The file was successfully saved as output.xlsx")

except FileNotFoundError:
    print("Error: File your_file.html not found.")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unknown error occurred: {e}")
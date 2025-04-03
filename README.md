# html2xlsx
This guide will help you export tables from HTML to XLSX format.




## 📦 Requirements

To use this code, make sure the following Python libraries are installed.  
We recommend installing them inside a virtual environment (`.venv`).

### 🧰 Required Libraries
```markdown
- beautifulsoup4  
- et_xmlfile  
- lxml  
- numpy  
- openpyxl  
- pandas  
- pip  
- python-dateutil  
- pytz  
- six  
- soupsieve  
- typing_extensions  
- tzdata  
```
### 🔧 Installation

1. **Create a virtual environment:**

```bash
python3 -m venv .venv
```

2. **Activate the virtual environment:**

- On macOS/Linux:
  ```bash
  source .venv/bin/activate
  ```
- On Windows:
  ```bash
  .venv\Scripts\activate
  ```

3. **Install dependencies:**

```bash
pip install beautifulsoup4 et_xmlfile lxml numpy openpyxl pandas python-dateutil pytz six soupsieve typing_extensions tzdata
```

Or you can use a `requirements.txt` file for convenience:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Use

Once all required libraries are installed in your virtual environment,  
you can run the provided script written in Python.

### 🛠️ Script Workflow

1. The script looks for a file named `your_file.html` in the directory where you run it.
2. It parses the HTML file and extracts any `<table>` elements.
3. The tables are then converted and saved as an Excel file named `output.xlsx`.

Make sure that:

- The HTML file contains at least one valid `<table>`.
- The file is named **exactly** `your_file.html` (or adjust the script accordingly).
- You have permission to read and write in the working directory.



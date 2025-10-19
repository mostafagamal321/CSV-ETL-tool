# csv-etl-tool

A lightweight ETL (Extract, Transform, Load) tool built in pure Python for working with CSV files.  
This tool allows you to:
- Read and inspect CSV files
- Check data quality (nulls and extra spaces)
- Clean and transform the data
- Generate simple numeric reports
- Export cleaned data to a new CSV
- All through an interactive terminal interface

---

## 🚀 Features

| Stage | Description |
|-------|-------------|
| Extract | Select an existing CSV file or provide a custom path |
| Check | Scan the file for null values and extra spaces (globally and per column) |
| Transform | Automatically clean data by replacing empty with `N/A` and trimming whitespace |
| Load | Save cleaned data to a new CSV file with `_new.csv` suffix |
| Report | Generate numeric insights such as sum, count, min, and max |

---

## 📂 Example Workflow

1. Run the tool
2. Choose a CSV file from your directory or attach your own path
3. View table structure and data quality summary
4. Transform & clean the data
5. View aggregated numeric reports

---

## 🛠️ Technologies Used

- **Python 3.10+**
- `csv` (built-in)
- `os` (built-in)
- `sys` (built-in)
- `re` (built-in)
- `prettytable` (for clean terminal tables)
- - `pytest` (for testing the functions)

Install PrettyTable if you don’t have it already:

```bash
pip install prettytable

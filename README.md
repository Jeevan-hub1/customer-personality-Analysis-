# Customer Personality Analysis: Data Cleaning and Preprocessing

## Overview
This project cleans and preprocesses the Customer Personality Analysis dataset from Kaggle to prepare it for analysis. The dataset contains customer demographic and purchase behavior data, with issues like missing values, duplicates, and inconsistent formats. The cleaning process is implemented using Python (Pandas) in the `task1.py` script.

## Dataset
- **Source:** Customer Personality Analysis on Kaggle  
- **Description:** ~2240 rows × ~29 columns (ID, Year_Birth, Education, Marital_Status, Income, Dt_Customer, purchase metrics)
- **Common Issues:**  
    - Missing values (e.g., in Income)  
    - Inconsistent text (e.g., "Graduation" vs. "graduate")  
    - Potential duplicates  
    - Incorrect data types

## Objectives
- Identify and handle missing values
- Remove duplicate rows
- Standardize text values (e.g., Education, Marital_Status)
- Convert dates to a consistent format and ensure correct data types
- Rename columns for uniformity
- Handle outliers (e.g., unrealistic ages, extreme incomes)
- Produce a cleaned dataset and summarize changes

## Requirements
- **Python:** 3.6+
- **Libraries:**  
    - Pandas (`pip install pandas`)
- **Dataset:** Download `customer_personality_analysis.csv` from Kaggle and place it in the project directory
- **Tools:** Any Python IDE (e.g., VS Code, PyCharm) or Jupyter Notebook

## File Structure
```
├── task1.py                                # Python script for data cleaning
├── customer_personality_analysis.csv        # Input dataset (download from Kaggle)
├── cleaned_customer_personality_analysis.csv # Output cleaned dataset (generated)
└── README.md                               # Project documentation
```

## Installation
1. Clone or download this repository.
2. Install required libraries:
     ```bash
     pip install pandas
     ```
3. Download the Customer Personality Analysis dataset from Kaggle and place `customer_personality_analysis.csv` in the project directory.

## Usage
1. Ensure `customer_personality_analysis.csv` is in the same directory as `task1.py`.
2. Run the script:
     ```bash
     python task1.py
     ```
     The script will:
     - Load the dataset
     - Perform cleaning steps (handle missing values, remove duplicates, standardize text, etc.)
     - Save the cleaned dataset as `cleaned_customer_personality_analysis.csv`
     - Print a summary of changes to the console

## Script Details
The `task1.py` script performs the following steps:
- **Load Dataset:** Reads the tab-separated CSV using Pandas
- **Rename Columns:** Converts column names to lowercase with underscores (e.g., `Year_Birth` → `year_birth`)
- **Handle Missing Values:** Fills income with median; drops rows with missing id
- **Remove Duplicates:** Deletes duplicate rows
- **Standardize Text:** Unifies education (e.g., "Graduation" → "graduate") and marital_status (e.g., "Together" → "married")
- **Convert Data Types:** Sets year_birth as int, dt_customer as datetime, income as float
- **Handle Outliers:** Filters ages (18–100 years) and caps income using the IQR method
- **Save Output:** Exports the cleaned dataset

## Example Output
```
Initial Dataset Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2240 entries, 0 to 2239
Data columns (total 29 columns):
...

Missing Values:
income    24
...

Number of duplicate rows: 0
...

Cleaned dataset saved as 'cleaned_customer_personality_analysis.csv'
```

## Deliverables
- **Cleaned Dataset:** `cleaned_customer_personality_analysis.csv`
- **Summary of Changes:** Printed to console and can be extracted from output:
    - Renamed columns to lowercase with underscores
    - Filled missing income values with median; dropped rows with missing id
    - Removed X duplicate rows (X depends on dataset)
    - Standardized education and marital_status values
    - Converted year_birth to int, dt_customer to datetime, income to float
    - Filtered ages to 18–100; capped income outliers
    - Final dataset contains Y rows (Y depends on cleaning results)

## Notes
- **Delimiter:** The dataset uses tabs (`\t`) as separators. The script handles this with `sep='\t'` in `pd.read_csv`.
- **Customizations:** Adjust the script for specific dataset issues (e.g., additional columns or different text inconsistencies).
- **Excel Alternative:** Cleaning can be done in Excel using filters for nulls/duplicates, text functions for standardization, and formatting for data types.

## Troubleshooting
- Ensure the dataset file path is correct
- Verify the delimiter if loading fails (open the CSV in a text editor)
- Check for Pandas installation (`pip show pandas`)
- Share console errors for debugging assistance

## Author
Created as part of a data preprocessing task.  
Contact: [Your Name/Email, if applicable]

## License
This project is for educational purposes and uses the Customer Personality Analysis dataset under its respective Kaggle license.

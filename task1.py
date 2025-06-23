
import pandas as pd

# Step 1: Load the dataset with tab delimiter
df = pd.read_csv(r"C:\Users\ponna\Downloads\archive (13)\marketing_campaign.csv", sep='\t')

# Initial inspection
print("Initial Dataset Info:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())

# Step 2: Rename columns for consistency (lowercase, replace spaces with underscores)
df.columns = [col.lower().replace(' ', '_') for col in df.columns]
print("\nColumns after renaming:")
print(df.columns)

# Step 3: Handle missing values
print("\nMissing Values:")
print(df.isnull().sum())
# Fill missing 'income' with median
df['income'] = df['income'].fillna(df['income'].median())
# Drop rows with missing critical fields (e.g., 'id')
df = df.dropna(subset=['id'])
print("\nMissing Values After Handling:")
print(df.isnull().sum())

# Step 4: Remove duplicates
print("\nNumber of duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()
print("Number of rows after removing duplicates:", len(df))

# Step 5: Standardize text values
df['education'] = df['education'].str.lower().replace({
    'graduation': 'graduate',
    'phd': 'phd',
    '2n cycle': 'basic',
    'master': 'masters'
})
df['marital_status'] = df['marital_status'].str.lower().replace({
    'single': 'single',
    'divorced': 'divorced',
    'together': 'married',
    'widow': 'widowed',
    'yolo': 'single',  # Handle unusual values if present
    'absurd': 'single'
})
print("\nUnique Education Values:")
print(df['education'].unique())
print("\nUnique Marital Status Values:")
print(df['marital_status'].unique())

# Step 6: Convert data types
df['year_birth'] = df['year_birth'].astype(int)
df['dt_customer'] = pd.to_datetime(df['dt_customer'], format='%d-%m-%Y', errors='coerce')
df['income'] = df['income'].astype(float)
print("\nData Types After Conversion:")
print(df.dtypes)

# Step 7: Handle outliers
df['age'] = 2025 - df['year_birth']  # Current year is 2025
df = df[df['age'].between(18, 100)]  # Keep realistic ages
# Cap extreme income values
q1 = df['income'].quantile(0.25)
q3 = df['income'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
df['income'] = df['income'].clip(lower=lower_bound, upper=upper_bound)
print("\nAge Range After Filtering:")
print(df['age'].describe())
print("\nIncome After Capping:")
print(df['income'].describe())

# Step 8: Save cleaned dataset
df.to_csv('cleaned_customer_personality_analysis.csv', index=False)
print("\nCleaned dataset saved as 'cleaned_customer_personality_analysis.csv'")
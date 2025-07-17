import pandas as pd
import os

# Load data
df = pd.read_csv("data/2024_fb_posts_president_scored_anon.csv")

# Create output folder
os.makedirs("output", exist_ok=True)

# Initialize result list
results = []

# Descriptive stats
for col in df.columns:
    col_data = df[col].dropna()
    row = {'Column': col, 'Count': col_data.shape[0]}
    
    if pd.api.types.is_numeric_dtype(col_data):
        row.update({
            'Type': 'Numeric',
            'Mean': round(col_data.mean(), 2),
            'Min': col_data.min(),
            'Max': col_data.max(),
            'StdDev': round(col_data.std(), 2)
        })
    else:
        row['Type'] = 'Categorical'
        vc = col_data.value_counts()
        row['Unique'] = col_data.nunique()
        for i, (val, count) in enumerate(vc.head(3).items()):
            row[f'Top_{i+1}_Value'] = val
            row[f'Top_{i+1}_Count'] = count
    results.append(row)

# Save to CSV
pd.DataFrame(results).to_csv("output/fb_posts_summary_pandas.csv", index=False)

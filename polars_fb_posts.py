import polars as pl
import os

# Load the dataset
df = pl.read_csv("data/2024_fb_posts_president_scored_anon.csv")
os.makedirs("output", exist_ok=True)

summary = []

for col in df.columns:
    col_data = df[col].drop_nulls()
    row = {"Column": col, "Count": col_data.len()}
    dtype = col_data.dtype

    if dtype in [pl.Int64, pl.Int32, pl.Float64, pl.Float32]:
        row["Type"] = "Numeric"
        row["Mean"] = round(col_data.mean(), 2)
        row["Min"] = col_data.min()
        row["Max"] = col_data.max()
        row["StdDev"] = round(col_data.std(), 2)

    elif dtype == pl.Utf8:
        row["Type"] = "Categorical"
        row["Unique"] = col_data.n_unique()
        
        vc = col_data.value_counts()
        vc = vc.rename({vc.columns[0]: "value", vc.columns[1]: "count"})
        vc_sorted = vc.sort("count", descending=True)
        
        for i, r in enumerate(vc_sorted.iter_rows()):
            if i >= 3:
                break
            row[f"Top_{i+1}_Value"] = r[0]
            row[f"Top_{i+1}_Count"] = r[1]

    summary.append(row)

# Save final summary to CSV
pl.DataFrame(summary).write_csv("output/fb_posts_summary_polars.csv")

import pandas as pd
import glob

# =========================
# Load all monthly files
# =========================

files = sorted(
    glob.glob("2024 Data/CRMLSListing2024*.csv")
)

dfs = []

total_before_concat = 0

for file in files:

    df = pd.read_csv(file)

    print(f"{file}: {len(df)} rows")

    total_before_concat += len(df)

    dfs.append(df)

print(
    f"Total rows before concatenation: {total_before_concat}"
)

# =========================
# Concatenate
# =========================

listing_df = pd.concat(
    dfs,
    ignore_index=True
)

print(
    f"Rows after concatenation: {len(listing_df)}"
)

# =========================
# Residential Filter
# =========================

print(
    f"Rows before Residential filter: {len(listing_df)}"
)

listing_df = listing_df[
    listing_df["PropertyType"] == "Residential"
]

print(
    f"Rows after Residential filter: {len(listing_df)}"
)

# =========================
# Save Output
# =========================

listing_df.to_csv(
    "Combined_Residential_Listings.csv",
    index=False
)

print(
    "Combined_Residential_Listings.csv created successfully."
)


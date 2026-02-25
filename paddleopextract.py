import pandas as pd
import re

#1. Load raw file
input_path  = "paddleop_3.csv"
output_path = "paddleop_3_cleaned.csv"

df = pd.read_csv(input_path, header=None)

#2. Keep only the first 3 columns
df = df.iloc[:, :3]

#3. Drop header rows (row 0 = "0,1,2" names; rows 1-3 = multi-line header)
df = df.drop([0, 1, 2, 3]).reset_index(drop=True)

#4. Rename columns 
df.columns = ["description", "quantity", "unit_price"]

#5. Extract serial numbers using regex 
#Pattern: sequences of uppercase letters & digits, 18+ characters long
SERIAL_PATTERN = r"[A-Z0-9]{18,}"

def extract_serials(text):
    if pd.isna(text):
        return None
    matches = re.findall(SERIAL_PATTERN, str(text))
    return ", ".join(matches) if matches else None

df["serial_no"] = df["description"].apply(extract_serials)

# ── 6. Save output ────────────────────────────────────────────────────────────
df.to_csv(output_path, index=False)

print(f"Done! Cleaned file saved to: {output_path}")
print(f"Shape: {df.shape}")
print(df.to_string())
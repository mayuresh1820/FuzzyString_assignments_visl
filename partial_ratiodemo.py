import pandas as pd
from rapidfuzz import fuzz

#master codes
master_codes = [
    "I-RD11017359",
    "I-RD11017360",
    "I-RD11017361",
    "I-RD11017256",
    "I-RD11017257"
]

#input codes
input_codes = [
    "RD11017355",
    "RD11017360",
    "RD11017361",
    "RD11017256",
    "RD11017257"
]

#convert master list to DataFrame
df_master = pd.DataFrame(master_codes, columns=["master_code"])

for inp in input_codes:
    best_score = 0
    best_match = None

    for _, row in df_master.iterrows():
        score = fuzz.partial_ratio(inp, row["master_code"])

        if score > best_score:
            best_score = score
            best_match = row["master_code"]

    # Decision logic
    if best_score >= 90:
        decision = "Auto select item"
    elif 70 <= best_score < 90:
        decision = "Send for manual review"
    else:
        decision = "Reject"

    print(f"\nInput Code: {inp}")
    print(f"Matched Master Code: {best_match}")
    print(f"Confidence: {best_score}%")
    print(f"Decision: {decision}")
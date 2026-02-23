import pandas as pd
from rapidfuzz import fuzz

items_input = [
    (" BW2001", "bubble wrap roll"),
    ("BW3002", "bubble wrap roll 3mm"),
    ("AK1010", "allen key set 10mm")
]

df_items = pd.DataFrame(items_input, columns=["item_code", "item_name"])

df_items.to_excel("items.xlsx", index=False)

queries = ["bubbl wrp rol", "bubbl wrp rol 3m","hlen kset"]

df = pd.read_excel("items.xlsx")

for q in queries:
    best_score, best_item, best_code = 0, None, None

    for _, row in df.iterrows():
        score = fuzz.token_sort_ratio(q, row["item_name"])
        if score > best_score:
            best_score = score
            best_item = row["item_name"]
            best_code = row["item_code"]



    print(f"\nQuery: {q}")
    print(f"Matched Item: {best_item}")
    print(f"Item Code: {best_code}")
    print(f"Confidence: {best_score}%")
    
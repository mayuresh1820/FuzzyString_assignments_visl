from rapidfuzz import fuzz

queries = ["bubbl wrp rol", "alen keyset", "disposable cupp"]
#queries = ["10mm Allen Key Set", "Stainless Steel Bolt 5mm"]

candidates = [
    "bubble wrap roll",
    "allen key set",
    "disposable cup",
    "flex print sheet"
]

# candidates = [
#     "Allen Key 10 mm",
#     "5mm SS Bolt",
# ]

for q in queries:
    print(f"\nQuery: {q}")
    for c in candidates:
        confidence = fuzz.token_sort_ratio(q, c)
        print(f"  {c} -> Confidence: {confidence}%")
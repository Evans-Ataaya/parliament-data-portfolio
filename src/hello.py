import pandas as pd

mps = pd.DataFrame({
    "name": ["Ama Example", "Kofi Sample", "Efua Demo"],
    "constituency": ["Constituency A", "Constituency B", "Constituency C"],
    "party": ["Party X", "Party Y", "Party X"],

})

print(mps)
mps.to_csv("data/processed/mps_demo.csv", index=False)
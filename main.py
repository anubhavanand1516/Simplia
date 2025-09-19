# main.py
from lead_generator import generate_leads
from lead_cleaner import clean_and_dedupe
from lead_scorer import score_and_classify

# 1. Generate synthetic leads
records = generate_leads(num_records=25)

# 2. Clean and dedupe
df, before, after = clean_and_dedupe(records)

# 3. Score and classify
df = score_and_classify(df)

# 4. Save CSV
out = "./homecare_leads.csv"
df.to_csv(out, index=False)

# 5. Print summary
print("Records before dedup:", before)
print("Records after dedup:", after)
print("Classification counts:\n", df['quality'].value_counts().to_string())
print("\nTop High-quality leads:")
print(df[df['quality']=='High'][['contact_name','business_name','phone','email','city','industry','score']].head(5).to_string(index=False))
print(f"\nCSV saved to {out}")

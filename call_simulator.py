# call_simulator.py
import pandas as pd

# Load leads
df = pd.read_csv('homecare_leads.csv')

# Three scripts as templates
script_A = """Hi {Name}, this is {Rep} from {Company}. 
We help {Industry} in {City} quickly arrange homecare for seniors/discharge cases. 
I see you’re looking to start soon — are you the decision-maker? 
Great! I can book a 20-minute intake call this week. 
Would Tuesday at 11 AM work?"""

script_B = """Hi {Name}, this is {Rep} from {Company}. 
We work with agencies and discharge teams, sharing resources on home transition planning. 
Would you like a quick PDF with our services? I’ll check back next month if that’s okay."""

script_C = """Hi {Name}, it’s {Rep} from {Company} — we spoke last week. 
You mentioned {Objection}. Have you had a chance to review our materials? 
I can send a case study and a proposed timeline to make the decision easier."""

def get_script(quality, row, rep="Anand", company="Simplia", objection="budget approval"):
    """Return the right script filled with lead info."""
    if quality == 'High':
        return script_A.format(Name=row['contact_name'],
                               Rep=rep,
                               Company=company,
                               Industry=row['industry'],
                               City=row['city'])
    elif quality == 'Low':
        return script_B.format(Name=row['contact_name'],
                               Rep=rep,
                               Company=company)
    else:  # Medium for follow-up example
        return script_C.format(Name=row['contact_name'],
                               Rep=rep,
                               Company=company,
                               Objection=objection)

# Demo: print 2 High-quality leads script A
print("=== Demo: High-quality leads ===")
for _, row in df[df['quality']=='High'].head(2).iterrows():
    print(get_script('High', row))
    print()

# Demo: 1 Low-quality lead script B
print("=== Demo: Low-quality lead ===")
row = df[df['quality']=='Low'].iloc[0]
print(get_script('Low', row))

# Demo: 1 Medium lead follow-up script C
print("=== Demo: Follow-up (Medium lead) ===")
row = df[df['quality']=='Medium'].iloc[0]
print(get_script('Medium', row))

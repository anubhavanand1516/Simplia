# lead_generator.py
import random
from datetime import datetime

nj_locations = [
    ("Newark","Essex"),("Jersey City","Hudson"),("Paterson","Passaic"),
    ("Elizabeth","Union"),("Edison","Middlesex"),("Woodbridge","Middlesex"),
    ("Lakewood","Ocean"),("Toms River","Ocean"),("Hamilton","Mercer"),
    ("Trenton","Mercer"),("Clifton","Passaic"),("Camden","Camden"),
    ("Cherry Hill","Camden"),("Princeton","Mercer"),("Morristown","Morris"),
]

industries = [
    "Home Health Agency","Senior Living","Nursing Home","Rehab / PT Center",
    "Palliative Care","Private Caregiver","Case Management","Pediatric Homecare"
]

target_demographics = [
    "Seniors","Caregivers","Case Managers","Discharge Planners","Nurses",
    "Children with disabilities","Guardians"
]

first_names = ["Grace","Liam","Olivia","Noah","Emma","Ava","Sophia","Jacob","Mason","Ethan","Michael","Sarah","Daniel","Laura"]
last_names = ["Johnson","Smith","Patel","Garcia","Davis","Brown","Miller","Wilson","Anderson","Thomas","Taylor","Moore"]

def make_phone():
    return f"+1-732-{random.randint(200,999)}-{random.randint(1000,9999)}"

def make_email(name,biz):
    local = name.lower().replace(" ",".")
    domain = biz.lower().replace(" ","").replace("&","") + ".com"
    return f"{local}@{domain}"

def make_business_name(name):
    suffixes = ["Care","Homecare Services","Assistance","Health","Senior Care","Home Support"]
    return f"{name} {random.choice(suffixes)}"

def generate_leads(num_records=25, seed=42):
    random.seed(seed)
    records=[]
    for i in range(num_records):
        fname = random.choice(first_names)
        lname = random.choice(last_names)
        contact_name = f"{fname} {lname}"
        biz_base = f"{lname}Care" if random.random() < 0.3 else f"{fname} & Co"
        business_name = make_business_name(biz_base)
        phone = make_phone()
        email = make_email(contact_name, biz_base)
        city, county = random.choice(nj_locations)
        industry = random.choice(industries)
        website_present = random.random() < 0.7
        budget_ready = random.random() < 0.35
        decision_maker_available = random.random() < 0.6
        purchase_timeline_days = random.randint(7,90)
        demographic_fit = random.choice(target_demographics)

        records.append({
            "contact_name": contact_name,
            "business_name": business_name,
            "phone": phone,
            "email": email,
            "city": city,
            "county": county,
            "industry": industry,
            "website_present": website_present,
            "budget_ready": budget_ready,
            "decision_maker_available": decision_maker_available,
            "purchase_timeline_days": purchase_timeline_days,
            "demographic_fit": demographic_fit,
            "created_at": datetime.now().isoformat(timespec='seconds'),
        })
    return records

# lead_scorer.py
import pandas as pd

def compute_score(row):
    score = 0
    score += 30 if row['budget_ready'] else 0
    score += 25 if row['decision_maker_available'] else 0
    if row['purchase_timeline_days'] <= 30:
        score += 20
    elif row['purchase_timeline_days'] <= 60:
        score += 10
    priority = {"Seniors","Case Managers","Discharge Planners","Nurses","Caregivers"}
    score += 15 if row['demographic_fit'] in priority else 0
    score += 10 if row['website_present'] else 0
    return score

def classify(score):
    if score >= 70: return "High"
    elif score >= 40: return "Medium"
    else: return "Low"

def score_and_classify(df: pd.DataFrame):
    df['score'] = df.apply(compute_score, axis=1)
    df['quality'] = df['score'].apply(classify)
    return df

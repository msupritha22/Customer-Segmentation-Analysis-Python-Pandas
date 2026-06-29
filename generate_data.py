# generate_data.py — Run this FIRST to create the customer dataset
import pandas as pd
import numpy as np
import os

np.random.seed(7)
os.makedirs("data", exist_ok=True)

n = 500

cities    = ["Bengaluru", "Mumbai", "Delhi", "Hyderabad", "Chennai",
             "Pune", "Kolkata", "Jaipur", "Ahmedabad", "Lucknow"]
platforms = ["App", "Website", "App", "App", "Website"]   # app-heavy
genders   = ["Male", "Female", "Male", "Female", "Other"]

records = []
for i in range(1, n + 1):
    age           = int(np.random.randint(18, 65))
    gender        = np.random.choice(genders, p=[0.45, 0.45, 0.04, 0.05, 0.01])
    city          = np.random.choice(cities)
    total_orders  = int(np.random.randint(1, 80))
    total_spent   = round(total_orders * np.random.uniform(300, 2500), 2)
    avg_order_val = round(total_spent / total_orders, 2)
    last_purchase = int(np.random.randint(1, 365))   # days ago
    platform      = np.random.choice(platforms)
    membership    = np.random.choice(["Free", "Silver", "Gold", "Platinum"],
                                     p=[0.50, 0.25, 0.15, 0.10])
    rating        = round(np.random.uniform(2.5, 5.0), 1)

    records.append({
        "customer_id":      f"CUST{i:04d}",
        "age":              age,
        "gender":           gender,
        "city":             city,
        "total_orders":     total_orders,
        "total_spent":      total_spent,
        "avg_order_value":  avg_order_val,
        "days_since_last_purchase": last_purchase,
        "platform":         platform,
        "membership_tier":  membership,
        "avg_rating_given": rating,
    })

df = pd.DataFrame(records)
df.to_csv("data/customers.csv", index=False)
print(f"✅ Dataset created: data/customers.csv  ({len(df)} rows)")

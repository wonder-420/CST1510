"""
RECORD CHECK  -  my version
===========================

Name  : Enrique Goromondo
Lane  : IT      
Date  : 07/11/2026

Run it:   python template.py
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/alyah/Desktop/CST1510/Week 6/LAB/miniproject6_record.csv")

"""add percent and status columns"""
df["percent"] = (df["value"] / df["limit"]) * 100
df["status"] = df.apply(lambda row: "OVER LIMIT" if row["percent"] > 100 else "WARNING" if row["percent"] > 90 else "OK", axis=1)

print(df)
print(df[df["status"] != "OK"])
print("counts per status:")
print(df.groupby("status").size())
df.to_csv("mini_project_records_report.csv", index=False)
df.groupby("status").size().plot(kind="bar")
plt.title("Count of Records by Status")
plt.savefig("mini_project_records_status_counts.png")
plt.show()

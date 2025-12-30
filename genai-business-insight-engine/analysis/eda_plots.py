import pandas as pd # type: ignore

df = pd.read_csv("customers.csv")

print(df.head())
print("\nColumns:")
print(df.columns)
import matplotlib.pyplot as plt

# Churn by plan
df["churned"] = df["churn_date"].notna()

churn_by_plan = (
    df.groupby("plan_type")["churned"]
    .mean()
    .reset_index()
)

plt.figure()
plt.bar(churn_by_plan["plan_type"], churn_by_plan["churned"])
plt.title("Churn Rate by Plan")
plt.ylabel("Churn Rate")
plt.xlabel("Plan Type")
plt.show()

# Revenue by plan
revenue_by_plan = df.groupby("plan_type")["monthly_fee"].mean()

plt.figure()
revenue_by_plan.plot(kind="bar")
plt.title("Average Monthly Revenue by Plan")
plt.ylabel("Monthly Fee")
plt.xlabel("Plan Type")
plt.show()

# Signup trend
df["signup_date"] = pd.to_datetime(df["signup_date"])

signup_trend = df.groupby(df["signup_date"].dt.to_period("M")).size()

plt.figure()
signup_trend.plot()
plt.title("Customer Signup Trend Over Time")
plt.ylabel("Customers")
plt.xlabel("Month")
plt.show()
plt.savefig("analysis/churn_rate.png")



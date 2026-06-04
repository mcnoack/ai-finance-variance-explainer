import pandas as pd

# Load fake sample data
data = pd.read_csv("sample_variance_data.csv")

# Calculate variance
data["Variance"] = data["Actual"] - data["Budget"]
data["Variance_Percent"] = data["Variance"] / data["Budget"]

# Sort by largest absolute variance
data["Abs_Variance"] = data["Variance"].abs()
top_variances = data.sort_values("Abs_Variance", ascending=False)

print("Top Variance Drivers")
print("--------------------")

for _, row in top_variances.iterrows():
    favorability = "unfavorable" if row["Variance"] > 0 else "favorable"
    amount = abs(row["Variance"])
    print(
        f"{row['Cost_Center']} was {favorability} by ${amount:,.0f}. "
        f"Primary driver: {row['Driver']}."
    )

print("\nDraft Leadership Commentary")
print("---------------------------")

unfavorable = data[data["Variance"] > 0]["Variance"].sum()
favorable = data[data["Variance"] < 0]["Variance"].sum()
net_variance = unfavorable + favorable

print(
    f"Overall results were unfavorable by ${net_variance:,.0f}. "
    f"The largest unfavorable drivers were related to labor and material cost increases. "
    f"These were partially offset by favorable contractor and maintenance spending. "
    f"Recommended follow-up areas include overtime usage, supplier price changes, "
    f"and quality inspection requirements."
)

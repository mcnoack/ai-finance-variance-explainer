import json
import pandas as pd
from pydantic import BaseModel, Field
import ollama

# 1. Pydantic Schema for Structured Output Validation
class VarianceCommentary(BaseModel):
    summary: str = Field(
        description="A 2-3 sentence executive narrative explaining net performance, primary cost drivers, and key offsets. Do NOT return a title or header."
    )
    key_risks: list[str] = Field(
        description="2-3 specific operational or financial risks tied directly to the unfavorable cost centers."
    )
    recommended_actions: list[str] = Field(
        description="2-3 concrete investigative inquiries for the finance analyst to pursue."
    )

# 2. Deterministic Financial Math via Pandas
def process_variances(filepath: str) -> tuple[pd.DataFrame, dict]:
    df = pd.read_csv(filepath)

    df["Variance"] = df["Actual"] - df["Budget"]
    df["Variance_Pct"] = (df["Variance"] / df["Budget"]) * 100
    df["Favorability"] = df["Variance"].apply(lambda x: "Unfavorable" if x > 0 else "Favorable")
    df["Abs_Variance"] = df["Variance"].abs()

    sorted_df = df.sort_values(by="Abs_Variance", ascending=False)

    unfavorable_sum = df.loc[df["Variance"] > 0, "Variance"].sum()
    favorable_sum = df.loc[df["Variance"] < 0, "Variance"].sum()
    net_variance = unfavorable_sum + favorable_sum

    metrics = {
        "net_variance": net_variance,
        "net_status": "Unfavorable" if net_variance > 0 else "Favorable",
        "total_unfavorable": unfavorable_sum,
        "total_favorable": favorable_sum,
        "line_items": sorted_df[["Cost_Center", "Variance", "Variance_Pct", "Favorability", "Driver"]].to_dict(orient="records"),
    }
    return sorted_df, metrics

# 3. Local Offline Model Inference (Air-Gapped)
def generate_leadership_commentary(metrics: dict, model_name: str = "llama3.2:3b") -> VarianceCommentary:
    prompt = f"""
You are a senior financial analyst writing commentary for executive leadership.
Write a clear, analytical review using the financial metrics provided below.

Context:
- Net Performance: ${metrics['net_variance']:,.2f} ({metrics['net_status']})
- Total Unfavorable Drift: ${metrics['total_unfavorable']:,.2f}
- Total Favorable Offsets: ${metrics['total_favorable']:,.2f}

Line Items:
{json.dumps(metrics['line_items'], indent=2)}

Guidelines:
1. Write a complete narrative in the summary field. Do NOT return a title, label, or headline.
2. Name the exact cost centers (e.g., Assembly Labor, Procurement) and their operational drivers.
3. State figures accurately based only on the numbers provided.
"""

    response = ollama.chat(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        format=VarianceCommentary.model_json_schema(),
        options={"temperature": 0.2},
    )
    return VarianceCommentary.model_validate_json(response["message"]["content"])

# 4. Pipeline Execution
if __name__ == "__main__":
    df, metrics = process_variances("sample_variance_data.csv")

    print("\n=== TOP VARIANCE DRIVERS (Deterministic Math) ===")
    for _, row in df.iterrows():
        print(
            f"{row['Cost_Center']:<22} | "
            f"{row['Favorability']:<11} | "
            f"${abs(row['Variance']):>10,.0f} ({row['Variance_Pct']:>+6.1f}%) | "
            f"Driver: {row['Driver']}"
        )

    print("\n=== GENERATING LOCAL AI COMMENTARY (Ollama Offline) ===")
    ai_output = generate_leadership_commentary(metrics)

    print("\nExecutive Summary:")
    print(ai_output.summary)

    print("\nKey Risks:")
    for risk in ai_output.key_risks:
        print(f"- {risk}")

    print("\nRecommended Analyst Inquiries:")
    for action in ai_output.recommended_actions:
        print(f"- {action}")
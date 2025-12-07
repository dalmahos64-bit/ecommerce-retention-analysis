# Generated with Jules (ChatGPT Codex)
# Customer Retention Analysis - 2024

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Retention": [68.88, 71.61, 74.91, 75.12]
}

df = pd.DataFrame(data)

# Compute average retention
average_retention = df["Retention"].mean()
print("Average Retention:", round(average_retention, 2))   # Should print 72.63

# Plot quarterly retention
plt.figure(figsize=(10, 5))
plt.plot(df["Quarter"], df["Retention"], marker="o", linewidth=2)
plt.axhline(y=85, linestyle="--", label="Industry Benchmark (85)")

plt.title("Customer Retention Rate - 2024")
plt.xlabel("Quarter")
plt.ylabel("Retention Rate")
plt.legend()

# Save chart
plt.savefig("retention_trend.png", dpi=300)
plt.close()

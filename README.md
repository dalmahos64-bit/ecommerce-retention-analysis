# E-commerce Customer Retention Analysis (2024)

**Email:** 23f2003561@ds.study.iitm.ac.in  
**Generated with:** Jules (ChatGPT Codex)

---

## 📊 Dataset Overview
This analysis focuses on the quarterly customer retention rates for 2024.

| Quarter | Retention Rate |
|--------|-----------------|
| Q1 | 68.88 |
| Q2 | 71.61 |
| Q3 | 74.91 |
| Q4 | 75.12 |

**Average Retention Rate:** **72.63**  
**Industry Target:** **85**

---

## 📈 Trend & Benchmark Comparison
The `analysis.py` script computes the quarterly metrics and generates a visualization (`retention_trend.png`) comparing the company’s performance with the industry benchmark of 85.

---

## 🔍 Key Findings

1. Retention has improved steadily from **68.88 in Q1 to 75.12 in Q4**, an overall increase of **6.24 points**.
2. The annual average of **72.63** is **12.37 points below** the industry benchmark.
3. The improvement rate slows between Q3 → Q4, suggesting plateauing effectiveness.
4. Despite positive momentum, growth is **not sufficient to close the benchmark gap** within 1–2 quarters.

---

## 💼 Business Implications

- Low customer retention increases acquisition cost and reduces customer lifetime value.
- Gap from industry benchmark indicates competitive disadvantage in customer loyalty.
- Declining relative performance threatens repeat revenue and fiscal year growth targets.
- Improvements are trending positive but not accelerating fast enough.

---

## 🎯 Recommendations

To improve retention and reach the target of 85, the company should:

1. **Implement targeted retention campaigns.** (Required solution)
2. Deploy customer segmentation for behavioral-based communication.
3. Create personalized loyalty rewards for high-value customers.
4. Launch re-engagement email automation for at-risk segments.
5. Analyze churn patterns using predictive analytics.

---

## 🧠 LLM Assistance Evidence

This repository was created using **Jules (ChatGPT Codex)** for:
- Code generation (`analysis.py`)
- Explanation and data story (`README.md`)
- Trend visualization logic

Commit history and comments reflect LLM involvement.




---

## 📁 Files Included

- `analysis.py` — Python script for all calculations and plot generation  
- `data.csv` — Dataset used for analysis  
- `retention_trend.png` — Visualization output  
- `README.md` — Full data story and recommendations  

---

## 📝 How to Run

```bash
pip install pandas matplotlib
python analysis.py

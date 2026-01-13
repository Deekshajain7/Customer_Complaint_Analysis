# 📊 Customer Complaint Analysis Project

> End-to-end data analytics project demonstrating data cleaning, SQL analysis, and visualization skills


## 📋 Project Overview

This project analyzes 25,000+ customer complaints for a fictional electronics retailer to identify service improvement opportunities. The analysis reveals actionable insights that could save $2M+ annually through reduced churn and operational efficiency.

**Business Context:** Customer satisfaction declined from 4.2 to 3.7 stars over 18 months. Management needs data-driven recommendations to reverse this trend.

---

## 🎯 Key Skills Demonstrated

- **Data Cleaning:** Handled duplicates, missing values, inconsistent formats, outliers
- **SQL Analysis:** Complex queries, joins, aggregations, window functions
- **Python:** Pandas, data manipulation, feature engineering
- **Data Visualization:** Matplotlib, Seaborn - created 13 professional charts
- **Business Analysis:** Translated data into actionable recommendations
- **Storytelling:** Communicated insights to non-technical stakeholders

---

## 🔍 Key Findings

1. **Product Quality Crisis:** 42% of complaints relate to quality, but only 28% are satisfactorily resolved
2. **Channel Inequality:** 300% difference in resolution time between fastest (social media: 18h) and slowest (email: 78h) channels
3. **VIP Neglect:** High-value customers get 8h slower service than regular customers
4. **Repeat Complaint Problem:** 35% are repeat issues, indicating poor initial resolution
5. **Holiday Overload:** Q4 complaints spike 65% with 4x longer resolution times

**💰 Business Impact:** Recommendations could save $2M+ annually with $550K investment (3.6x ROI)

---

## 📁 Project Structure

```
customer-complaint-analysis/
│
├── data/
│   ├── customer_complaints_raw.csv          # Original dataset
│   ├── customer_complaints_cleaned.csv      # After cleaning
│   ├── customer_complaints_enriched.csv     # With engineered features
│   └── complaints_analysis.db               # SQLite database
│
├── sql_results/
│   ├── q1_monthly_trends.csv
│   ├── q2_complaint_categories.csv
│   └── ... (12 query result files)
│
├── visualizations/
│   ├── 01_monthly_trends.png
│   ├── 02_complaint_categories.png
│   └── ... (13 visualization files)
│
├── scripts/
│   ├── generate_data.py                     # Create synthetic dataset
│   ├── day2_cleaning.py                     # Data cleaning pipeline
│   ├── day3_features.py                     # Feature engineering
│   ├── day3_sql_export.py                   # Export to SQL
│   ├── day4_sql_queries.py                  # SQL analysis queries
│   ├── day5_visualizations.py               # Charts (Part 1)
│   └── day6_advanced_viz.py                 # Charts (Part 2)
│
├── Final_Report.md                          # Comprehensive business report
├── README.md                                # This file
└── requirements.txt                         # Python dependencies
```

---

## 🚀 How to Run This Project

### Prerequisites
```bash
Python 3.8+
pandas
matplotlib
seaborn
sqlite3
```

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/customer-complaint-analysis.git
cd customer-complaint-analysis

# Install dependencies
pip install -r requirements.txt
```

### Run Analysis (Step by Step)
```bash
# Step 1: Generate synthetic dataset
python scripts/generate_data.py

# Step 2: Clean the data
python scripts/day2_cleaning.py

# Step 3: Create features and export to SQL
python scripts/day3_features.py
python scripts/day3_sql_export.py

# Step 4: Run SQL analysis
python scripts/day4_sql_queries.py

# Step 5 & 6: Create visualizations
python scripts/day5_visualizations.py
python scripts/day6_advanced_viz.py
```

---

## 📊 Sample Visualizations

### Monthly Complaint Trends
![Monthly Trends](visualizations/01_monthly_trends.png)

### Complaint Categories Distribution
![Categories](visualizations/02_complaint_categories.png)

### Executive Dashboard
![Dashboard](visualizations/13_executive_dashboard.png)

*View all 13 visualizations in the `/visualizations` folder*

---

## 💡 Key Technical Highlights

### Data Cleaning Challenges Solved
- ✅ Standardized 4 different date formats into ISO 8601
- ✅ Removed 487 duplicate complaint records
- ✅ Handled 30% missing satisfaction scores intelligently
- ✅ Fixed outlier resolution times (0h and 9999h values)
- ✅ Cleaned inconsistent text (case sensitivity, extra spaces, typos)

### Advanced SQL Queries
```sql
-- Example: Customer segment analysis with window functions
SELECT 
    customer_segment,
    complaint_category,
    COUNT(*) as complaints,
    AVG(resolution_time_hours) as avg_resolution,
    RANK() OVER (PARTITION BY customer_segment ORDER BY COUNT(*) DESC) as category_rank
FROM complaints
GROUP BY customer_segment, complaint_category
ORDER BY customer_segment, category_rank;
```

### Feature Engineering
Created 13 new analytical features:
- Time-based: Year, Month, Quarter, Day of Week
- Categorical: Complaint type (7 categories)
- Performance: Resolution speed buckets
- Segmentation: High-value customer flag, Customer tenure groups
- Boolean flags: Weekend, Holiday season, Repeat complaint

---

## 📈 Business Recommendations

### Immediate Actions (0-30 days)
1. **Fix product packaging** for top 3 problem products → Save $250K/year
2. **Launch VIP fast-track** support queue → Retain $1.2M revenue
3. **Intervene in underperforming stores** (#7, #12) → Improve satisfaction 35%

### Short-term (1-3 months)
4. Standardize email response process → Reduce resolution time 38%
5. Build self-service knowledge base → Deflect 30% of tickets
6. Hire seasonal Q4 support staff → Maintain service during peak

### Long-term (6-12 months)
7. Implement predictive complaint system → Reduce volume 25%
8. Optimize all channels to social media standards → <48h resolution
9. Launch quality assurance program → Cut repeat complaints 57%

**Expected Outcome:** Satisfaction 3.7 → 4.3, Resolution time 58h → 36h

---

## 🎓 What I Learned

- **Data isn't perfect:** Real-world data requires significant cleaning (20% of project time)
- **Context matters:** Same metric means different things in different business contexts
- **Visualization is storytelling:** Charts should answer "so what?" not just "what?"
- **SQL is powerful:** Complex business questions often need just 10-15 lines of SQL
- **Actionability beats perfection:** 80% accuracy with clear recommendations > 95% accuracy with vague insights

---

## 🔮 Future Enhancements

- [ ] Build interactive dashboard with Plotly/Streamlit
- [ ] Add sentiment analysis on complaint text using NLP
- [ ] Create predictive model for complaint resolution time
- [ ] Implement automated anomaly detection
- [ ] Add geographic analysis if location data available

---

## 👤 About This Project
**Author:** Deeksha Jain

**Role:** Data Analyst

**Project Type:** Portfolio Project - Data Analytics

**Duration:** 7 days (learning project)

**Date:** 2025

Contact: deekshadineshjain@gmail.com | https://www.linkedin.com/in/deekshajain7


---

## 📄 License

This project uses synthetic data and is intended for educational/portfolio purposes.

---


## ⭐ If you found this project helpful, please give it a star!


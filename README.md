# 🍎 Apple Global Sales Data Analysis

> A beginner-level exploratory data analysis (EDA) project using Python, built in Google Colab. This project explores Apple's global sales dataset across multiple dimensions including product categories, geographic regions, sales channels, and customer behavior.

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Dataset Description](#-dataset-description)
- [Dataset Columns](#-dataset-columns)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Key Analyses Performed](#-key-analyses-performed)
- [Key Findings & Conclusions](#-key-findings--conclusions)
- [Data Quality Notes](#-data-quality-notes)
- [Statistical Summary](#-statistical-summary)
- [How to Run](#-how-to-run)
- [Author](#-author)

---

## 🔍 Project Overview

This project is a **beginner-level data science project** that performs **Exploratory Data Analysis (EDA)** on Apple's global sales dataset using Python and popular data science libraries. The dataset contains **11,500 transaction records** spanning **2022–2024**, covering multiple countries, product categories, and customer segments.

The goal of this analysis is to uncover meaningful patterns in Apple's global sales data including:
- How product prices relate to discounted prices
- Regional revenue differences based on product pricing
- The impact of foreign exchange (FX) rates on local currency revenue

---

## 📦 Dataset Description

| Property | Value |
|---|---|
| **File Name** | `apple_global_sales_dataset.csv` |
| **Number of Records** | 11,500 |
| **Number of Columns** | 27 |
| **Time Period** | 2022 – 2024 |
| **Sample Countries** | Argentina, and many more globally |
| **Data Source** | Apple Global Sales (synthetic/simulated dataset) |

---

## 🗂️ Dataset Columns

| # | Column | Data Type | Description | Missing Values |
|---|--------|-----------|-------------|----------------|
| 0 | `sale_id` | object | Unique sale identifier (e.g., APPL-00000001) | 0 |
| 1 | `sale_date` | object | Date of the sale | 0 |
| 2 | `year` | int64 | Year of the sale (2022–2024) | 0 |
| 3 | `quarter` | object | Quarter of the sale (Q1–Q4) | 0 |
| 4 | `month` | object | Month of the sale | 0 |
| 5 | `country` | object | Country where the sale occurred | 0 |
| 6 | `region` | object | Geographic region (e.g., South America, Asia) | 0 |
| 7 | `city` | object | City where the sale occurred | 0 |
| 8 | `product_name` | object | Name of the Apple product sold | 0 |
| 9 | `category` | object | Product category (iPhone, Mac, AirPods, Apple Watch, Accessories, etc.) | 0 |
| 10 | `storage` | object | Storage capacity (where applicable) | **4,804 missing** |
| 11 | `color` | object | Product color | 0 |
| 12 | `unit_price_usd` | float64 | Unit price in US Dollars | 0 |
| 13 | `discount_pct` | int64 | Discount percentage applied (0–15%) | 0 |
| 14 | `units_sold` | int64 | Number of units sold per transaction | 0 |
| 15 | `discounted_price_usd` | float64 | Final price after discount in USD | 0 |
| 16 | `revenue_usd` | float64 | Total revenue in USD | 0 |
| 17 | `currency` | object | Local currency code (e.g., ARS for Argentina) | 0 |
| 18 | `fx_rate_to_usd` | float64 | Foreign exchange rate to USD | 0 |
| 19 | `revenue_local_currency` | float64 | Revenue in local currency | 0 |
| 20 | `sales_channel` | object | Channel of sale (Apple Store, Third-Party Retailer, Authorized Reseller, Corporate/B2B, Carrier Store) | 0 |
| 21 | `payment_method` | object | Payment method (Cash, Debit Card, Credit Card, Net Banking, etc.) | 0 |
| 22 | `customer_segment` | object | Customer segment (Individual, Business, Government, Education) | 0 |
| 23 | `customer_age_group` | object | Age group of customer (e.g., 18–24, 45–54) | 0 |
| 24 | `previous_device_os` | object | Previous device OS (for switcher analysis) | **8,056 missing** |
| 25 | `customer_rating` | float64 | Customer satisfaction rating (3.0–5.0 scale) | **3,360 missing** |
| 26 | `return_status` | object | Whether the item was kept or returned | 0 |

---

## 🛠️ Tech Stack

| Tool / Library | Purpose |
|---|---|
| **Python 3** | Primary programming language |
| **Pandas** | Data loading, manipulation, and analysis |
| **Matplotlib** | Base plotting library |
| **Seaborn** | Statistical data visualization |
| **Google Colab** | Cloud-based Jupyter notebook environment |

---

## 📁 Project Structure

```
Apple-Global-Sales-Data-Analysis/
│
├── Untitled12.ipynb              # Main analysis notebook (Google Colab)
├── apple_global_sales_dataset.csv  # Dataset (loaded in Colab)
├── Screen-Recording (2).mp4     # Demo/walkthrough video
└── README.md                    # Project documentation
```

---

## 🔬 Key Analyses Performed

### 1. 📥 Data Loading & Inspection
- Loaded the dataset using `pandas.read_csv()`
- Previewed data with `df.head()` to understand structure and sample values
- Used `df.info()` to examine column types and non-null counts
- Computed missing values with `df.isnull().sum()`

### 2. 📊 Descriptive Statistics
- Ran `df.describe()` to get summary statistics for all numeric columns:
  - Mean unit price: **~$807.85 USD**
  - Max unit price: **$7,551.01 USD** (high-end Mac/Pro models)
  - Average units sold per transaction: **~2.02 units**
  - Average discount: **~3.84%**, with a max of **15%**
  - Average revenue per transaction: **~$1,568.32 USD**
  - Average customer rating: **~4.0 / 5.0**

### 3. 📈 Scatter Plot Analysis (Unit Price vs. Discounted Price)
- Used `sns.relplot()` to visualize the relationship between **unit price** and **discounted price**

### 4. 🌍 Regional Revenue Analysis (Unit Price vs. Revenue by Region)
- Visualized **unit price vs. local currency revenue** with region as the hue
- Identified regional sales patterns across Asia, South America, and other global regions

### 5. 💱 FX Rate Impact on Revenue (Line Plot)
- Plotted a **line chart** showing how **exchange rate to USD** affects **local currency revenue**
- Used `kind="line"` with `sns.relplot()` to surface currency-driven revenue effects

---

## 📌 Key Findings & Conclusions

### 💡 Conclusion 1 – Price vs. Discount Relationship
> **There is a strong positive relationship between unit price and discounted price.** Discounted prices increase proportionally with unit prices. However, higher-priced products appear to receive larger **absolute discount amounts**, suggesting aggressive discount strategies are applied specifically to premium-tier products.

### 💡 Conclusion 2 – Regional Revenue Patterns
> **The Asian region generates relatively higher revenue at lower unit prices compared to other regions.** This suggests **stronger demand or higher sales volume** in Asia for more affordable Apple products, highlighting the importance of mid-range pricing strategies for Asian markets.

### 💡 Conclusion 3 – FX Rate & Local Currency Revenue
> **Revenue in local currency tends to spike significantly when the exchange rate to USD reaches extreme levels (around 16,000).** This indicates that **currency fluctuations strongly influence reported local currency revenue** — a higher exchange rate may artificially inflate local currency revenue values without reflecting actual volume growth.

---

## ⚠️ Data Quality Notes

| Column | Issue | Count | Notes |
|--------|-------|-------|-------|
| `storage` | Missing values | 4,804 | Expected — accessories and services have no storage |
| `previous_device_os` | Missing values | 8,056 | Majority of customers didn't provide switcher data |
| `customer_rating` | Missing values | 3,360 | Not all customers submitted ratings |

> **Note:** Most missing values are **expected and contextually valid** — for example, accessories like USB-C cables don't have a storage capacity, and not all customers provide ratings or previous OS information.

---

## 📐 Statistical Summary

| Metric | Value |
|--------|-------|
| Total Records | 11,500 |
| Years Covered | 2022, 2023, 2024 |
| Avg Unit Price (USD) | $807.85 |
| Max Unit Price (USD) | $7,551.01 |
| Min Unit Price (USD) | $26.69 |
| Avg Revenue per Transaction (USD) | $1,568.32 |
| Max Revenue per Transaction (USD) | $59,529.52 |
| Avg Discount | 3.84% |
| Max Discount | 15% |
| Avg Units Sold | 2.02 units |
| Max Units Sold | 8 units |
| Avg Customer Rating | 4.0 / 5.0 |
| Max FX Rate | 24,500 (to USD) |

---

## ▶️ How to Run

### Option 1: Google Colab (Recommended)
1. Open [Google Colab](https://colab.research.google.com/)
2. Upload `Untitled12.ipynb` to Colab
3. Upload `apple_global_sales_dataset.csv` to the Colab session storage
4. Run all cells sequentially

### Option 2: Local Jupyter Notebook
```bash
# 1. Clone the repository
git clone https://github.com/Rajapakshaminindu/Apple-Global-Sales-Data-Analysis.git
cd Apple-Global-Sales-Data-Analysis

# 2. Install dependencies
pip install pandas matplotlib seaborn jupyter

# 3. Launch Jupyter
jupyter notebook Untitled12.ipynb
```

> **Prerequisites:** Python 3.x, pip

---

## 👤 Author

**Rajapakshaminindu**  
- 📂 GitHub: [@Rajapakshaminindu](https://github.com/Rajapakshaminindu)

---

> 🚀 *This is a beginner-level data science project focused on exploratory data analysis using Python and Google Colab. Contributions and suggestions are welcome!*

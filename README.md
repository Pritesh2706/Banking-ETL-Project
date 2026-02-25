# 🏦 End-to-End Banking ETL Data Engineering Project

## 📌 Project Overview

This project demonstrates an end-to-end Data Engineering pipeline built using AWS, Databricks, and PySpark following the Medallion Architecture (Bronze → Silver → Gold).

The pipeline ingests raw banking transaction data from AWS S3, processes and cleans the data in Databricks using PySpark, and transforms it into analytics-ready Gold tables for interactive dashboard visualization.

This project is designed to simulate a real-world banking analytics system used for business insights, KPI tracking, and advanced transaction analysis.

---

## 🧱 Architecture (Medallion Architecture)

```
AWS S3 (Raw Data)
        ↓
Bronze Layer (Raw Delta Table)
        ↓
Silver Layer (Cleaned & Transformed Data)
        ↓
Gold Layer (Aggregated Analytics Tables)
        ↓
Databricks Dashboard (Visualization)
```

---

## 🛠️ Tech Stack

* AWS S3 (Data Storage)
* Databricks (Data Processing & Analytics)
* PySpark (ETL & Transformations)
* Delta Lake (Data Lakehouse Storage)
* Databricks SQL Dashboard (Visualization)
* Python

---

---

## 🔐 AWS IAM Role & Permissions

To ensure secure and production-grade cloud access, a dedicated AWS IAM Role was created and configured for this project.

### Configuration Details:
- Created a custom IAM Role for Databricks-S3 integration
- Configured role-based authentication (no hardcoded access keys)
- Attached S3 permissions for Medallion data layers (Bronze, Silver, Gold)
- Region aligned with Databricks workspace for seamless connectivity

### Permissions Granted:
- Read/Write access to S3 bucket: `s3://banking-etl-project-01/`
- Access to raw, processed, and analytics data layers
- Secure cross-service access between AWS S3 and Databricks

Purpose: Enable secure, scalable, and production-ready ETL pipeline integration between AWS S3 and Databricks. 

---

## 📂 Dataset

* File: `banking_etl-project.csv`
* Records: 500 transactions
* Contains:

  * transaction_id
  * account_id
  * customer_id
  * transaction_amount
  * transaction_type
  * channel
  * merchant_country

The dataset includes null values, duplicates, and mixed transaction types to simulate real-world banking data.

---

## 🔶 Bronze Layer (Raw Data Ingestion)

### Description:

* Raw CSV data is stored in AWS S3
* Loaded into Databricks as-is
* No transformation applied

### Key Steps:

* Create S3 bucket
* Upload raw dataset
* Read data using PySpark
* Store as Bronze Delta table

Purpose: Preserve original data for traceability and auditing.

---

## 🥈 Silver Layer (Data Cleaning & Transformation)

### Description:

The Silver layer focuses on data cleaning, deduplication, and null handling.

### Transformations Performed:

* Removed duplicate records
* Handled null values (numeric & categorical)
* Dropped records with missing critical IDs (account_id)
* Added ingestion timestamp
* Schema standardization

### Example Cleaning Logic:

* Filled `transaction_amount` nulls with 0
* Filled categorical columns with "Unknown"
* Ensured data quality for analytics

Purpose: Create a clean, reliable dataset for business analysis.

---

## 🥇 Gold Layer (Business Aggregations)

The Gold layer contains aggregated, analytics-ready tables used for dashboards and reporting.

### 1️⃣ KPI Summary Table

Table: `banking.gold.kpi_summary`

* Total Transactions
* Total Amount
* Average Transaction Amount

### 2️⃣ Account-wise Summary

Table: `banking.gold.account_summary`

* Total transactions per account
* Total transaction amount per account

### 3️⃣ Transaction Type Analysis

Table: `banking.gold.transaction_type_summary`

* Debit vs Credit distribution
* Total amount by transaction type

### 4️⃣ Channel & Country Analysis

Table: `banking.gold.channel_country_summary`

* Channel performance analysis
* Country-wise transaction insights

Purpose: Enable fast querying and dashboard visualization.

---

## 📊 Dashboard (Databricks SQL Dashboard)

A two-page interactive dashboard was created using Gold tables.

### Page 1: Banking Analytics Dashboard (Executive Summary)

* KPI Cards (Total Transactions, Total Amount, Avg Transaction)
* Top Accounts by Total Amount
* Transaction Type Pie Chart

### Page 2: Transaction & Channel Deep Dive

* Channel vs Country (Stacked Bar Chart)
* Top Accounts by Transaction Volume
* Transaction Type Breakdown
* Advanced analytics insights

The dashboard provides business-ready insights similar to real banking analytics systems.

---

## 🚀 Key Features

* End-to-End ETL Pipeline
* Medallion Architecture Implementation
* AWS + Databricks Integration
* Delta Lake for scalable storage
* Data Quality Handling (Nulls & Duplicates)
* Aggregated Gold Layer for BI
* Interactive Dashboard Visualization

---

## 📈 Business Use Cases

* Banking KPI Monitoring
* Customer Transaction Analysis
* Channel Performance Tracking
* Country-wise Transaction Insights
* Fraud Pattern Exploration (Negative Transactions)

---

## 👨‍💻 Author

Data Engineering Project using AWS + Databricks + PySpark

---

## ⭐ Future Improvements

* Real-time streaming ingestion (Kafka)
* Automated orchestration using Airflow
* CI/CD pipeline for ETL jobs
* Advanced fraud detection models  

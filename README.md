# twitter-airflow-aws-pipeline
An end-to-end Data Engineering pipeline built using Apache Airflow, Python, Pandas, AWS EC2, and AWS S3 to automate mock ETL workflows.



# 🚀 End-to-End Data Engineering Pipeline: Twitter ETL with Apache Airflow & AWS

An automated, zero-cost (₹0) data pipeline built to simulate real-world data engineering workflows, orchestrating ETL tasks using Apache Airflow deployed on an AWS EC2 cloud instance and storing transformed data into AWS S3.

---

## 🛠️ Architecture & Tech Stack
* **Orchestration:** Apache Airflow (`DAGs`, `PythonOperators`)
* **Compute & Hosting:** AWS EC2 (Ubuntu Linux, configured with Swap memory for optimal stability)
* **Storage / Data Lake:** AWS S3 (`zenithpro-airflow-bucket`)
* **Data Processing:** Python, Pandas, Boto3 / S3FS
* **Data Source:** Custom mock-data generator function simulating real-time social media ingestion.

---

## ⚙️ Pipeline Workflow
1. **Extract:** Python mock-generator creates structured social media records (`twitter_etl.py`).
2. **Transform:** Pandas cleans, structures, and converts raw JSON/dictionary data into a refined Data Frame.
3. **Load:** Automatically pushes and stores the processed dataset as a `.csv` file into an AWS S3 bucket.
4. **Orchestrate:** Scheduled and managed seamlessly via Apache Airflow DAGs (`twitter_dag.py`).


## ⚙️ data Pipeline architecture
[ Raw Data Source ]  --->  [ AWS EC2 / Python ]  --->  [ Apache Airflow ]  --->  [ AWS S3 Data Lake ]
(e.g. Tweets / APIs)       (Extract & Clean Data)     (Automate & Schedule)     (Central Clean Storage)

---
## 📂 Project Structure
├── airflow/
│   ├── dags/
│   │   ├── twitter_dag.py     # Airflow DAG orchestration script
│   │   └── twitter_etl.py     # Core ETL and S3 upload logic

💡 Key Learnings & Highlights
Successfully deployed and managed Apache Airflow on a remote Ubuntu cloud server via SSH.
Resolved cloud memory constraints on micro-instances by implementing custom Linux swap space.
Implemented IAM roles and policies to securely authorize EC2-to-S3 cloud data transfers.



****FOR MORE INFORMATION CHECK THE YT VIDEO :- https://youtu.be/q8q3OFFfY6c?si=x5F7EopNXgJUue4T

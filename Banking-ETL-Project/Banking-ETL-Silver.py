# Databricks notebook source
spark.sql("CREATE SCHEMA IF NOT EXISTS banking.silver")

# COMMAND ----------

import pyspark.sql.functions as F
from pyspark.sql.types import StringType, IntegerType, DoubleType, TimestampType, FloatType

catalog_name ='banking'

# COMMAND ----------

df = spark.read.format("csv") \
    .option("header", True) \
    .option("inferSchema", True) \
    .load("s3://banking-etl-project-01/raw/")

display(df)


# COMMAND ----------

# MAGIC %md
# MAGIC Rename Columns

# COMMAND ----------

# Standardize column names (lowercase + underscore)
silver_df = df.toDF(*[c.lower().replace(" ", "_") for c in df.columns])

display(silver_df)


# COMMAND ----------

# MAGIC %md
# MAGIC Remove Duplicates

# COMMAND ----------

# Remove duplicate records
silver_df = silver_df.dropDuplicates()

print("Row count after removing duplicates:", silver_df.count())


# COMMAND ----------

# MAGIC %md
# MAGIC Handle Null Values

# COMMAND ----------

from pyspark.sql.functions import col

# Drop critical nulls (adjust column names based on your dataset)
silver_df = silver_df.dropna(subset=[
    "transaction_id",
    "customer_id",
    "transaction_amount"
])


# COMMAND ----------

# Fill numeric columns
silver_df = silver_df.fillna({
    "transaction_amount": 0,
    "transaction_id": 0,
    "customer_id" : 0,
    "transaction_timestamp" : 0
})

# Fill string columns
silver_df = silver_df.fillna({
    "transaction_type": "Unknown",
    "channel": "Unknown",
    "merchant_country": "Unknown"
})

# Drop only critical null account_id
silver_df = silver_df.dropna(subset=["account_id"])

# COMMAND ----------

# MAGIC %md
# MAGIC Fix Data Types

# COMMAND ----------

from pyspark.sql.functions import col

silver_df = silver_df \
    .withColumn("transaction_id", col("transaction_id").cast("int")) \
    .withColumn("transaction_amount", col("transaction_amount").cast("double"))


# COMMAND ----------

# MAGIC %md
# MAGIC Derived Columns

# COMMAND ----------

from pyspark.sql.functions import current_timestamp

silver_df = silver_df.withColumn("ingestion_timestamp", current_timestamp())


# COMMAND ----------

# MAGIC %md
# MAGIC Save Silver Table

# COMMAND ----------

silver_df.write.format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("banking.silver.banking_clean")


# COMMAND ----------

display(spark.table("banking.silver.banking_clean"))


# COMMAND ----------

print("Bronze Count:", df.count())
print("Silver Count:", silver_df.count())

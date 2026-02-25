# Databricks notebook source
from pyspark.sql.functions import current_timestamp, expr, col

# Use your catalog and schema
spark.sql("USE CATALOG banking")
spark.sql("USE SCHEMA default")

# Step 1: Read CSV from S3 raw folder
df = spark.read \
    .format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("mode", "PERMISSIVE") \
    .load("s3://banking-etl-project-01/raw/")

# Step 2: Add metadata columns (UC supported)
df_bronze = df \
    .withColumn("ingested_at", current_timestamp()) \
    .withColumn("source_file", col("_metadata.file_path")) \
    .withColumn("bronze_id", expr("uuid()"))

# Step 3: Write to Managed Delta Table (NO S3 PATH)
df_bronze.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("banking.default.banking_etl_project")

print("✅ SUCCESS: S3 raw → Bronze Managed Delta Table loaded")


# COMMAND ----------

df = spark.read.format("csv") \
    .option("header", True) \
    .option("inferSchema", True) \
    .load("s3://banking-etl-project-01/raw/")

display(df)

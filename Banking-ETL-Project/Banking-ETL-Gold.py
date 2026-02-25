# Databricks notebook source
spark.sql("CREATE SCHEMA IF NOT EXISTS banking.gold")


# COMMAND ----------

silver_df = spark.table("banking.silver.banking_clean")
display(silver_df)


# COMMAND ----------

# MAGIC %md
# MAGIC KPI Summary

# COMMAND ----------

from pyspark.sql.functions import count, sum, avg

gold_kpi_df = silver_df.agg(
    count("transaction_id").alias("total_transactions"),
    sum("transaction_amount").alias("total_amount"),
    avg("transaction_amount").alias("avg_transaction_amount")
)

display(gold_kpi_df)


# COMMAND ----------

gold_kpi_df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("banking.gold.kpi_summary")


# COMMAND ----------

# MAGIC %md
# MAGIC Account-wise Summary

# COMMAND ----------

from pyspark.sql.functions import sum, count

gold_account_df = silver_df.groupBy("account_id").agg(
    count("transaction_id").alias("total_transactions"),
    sum("transaction_amount").alias("total_amount")
)

display(gold_account_df)


# COMMAND ----------

gold_account_df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("banking.gold.account_summary")


# COMMAND ----------

# MAGIC %md
# MAGIC Transaction Type Analysis

# COMMAND ----------

gold_txn_type_df = silver_df.groupBy("transaction_type").agg(
    count("transaction_id").alias("total_transactions"),
    sum("transaction_amount").alias("total_amount")
)

display(gold_txn_type_df)


# COMMAND ----------

gold_txn_type_df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("banking.gold.transaction_type_summary")


# COMMAND ----------

# MAGIC %md
# MAGIC Channel & Country Analysis

# COMMAND ----------

gold_channel_country_df = silver_df.groupBy(
    "channel",
    "merchant_country"
).agg(
    count("transaction_id").alias("total_transactions"),
    sum("transaction_amount").alias("total_amount")
)

display(gold_channel_country_df)


# COMMAND ----------

gold_channel_country_df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("banking.gold.channel_country_summary")

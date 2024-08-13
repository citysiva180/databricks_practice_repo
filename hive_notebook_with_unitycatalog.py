# Databricks notebook source
# MAGIC %sql
# MAGIC USE CATALOG hive_metastore

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE employees
# MAGIC   (id INT, name STRING, salary DOUBLE);

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO employees
# MAGIC VALUES 
# MAGIC   (1, "Adam", 3500.0),
# MAGIC   (2, "Sarah", 4020.5);
# MAGIC
# MAGIC INSERT INTO employees
# MAGIC VALUES
# MAGIC   (3, "John", 2999.3),
# MAGIC   (4, "Thomas", 4000.3);
# MAGIC
# MAGIC INSERT INTO employees
# MAGIC VALUES
# MAGIC   (5, "Anna", 2500.0);
# MAGIC
# MAGIC INSERT INTO employees
# MAGIC VALUES
# MAGIC   (6, "Kim", 6200.3)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM employees

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL employees

# COMMAND ----------

# MAGIC %fs ls 'dbfs:/user/hive/warehouse/employees'

# COMMAND ----------

# MAGIC %sql
# MAGIC UPDATE employees 
# MAGIC SET salary = salary + 100
# MAGIC WHERE name LIKE "A%"

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM employees

# COMMAND ----------

# MAGIC %fs ls 'dbfs:/user/hive/warehouse/employees'

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL employees

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM employees

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY employees

# COMMAND ----------

# MAGIC %fs ls 'dbfs:/user/hive/warehouse/employees/_delta_log'

# COMMAND ----------

# MAGIC %fs head 'dbfs:/user/hive/warehouse/employees/_delta_log/00000000000000000005.json'

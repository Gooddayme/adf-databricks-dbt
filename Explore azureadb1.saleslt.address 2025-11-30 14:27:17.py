# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC     select
# MAGIC       *
# MAGIC     from (
# MAGIC       
# MAGIC     
# MAGIC   
# MAGIC
# MAGIC with scd as (
# MAGIC     select
# MAGIC         AddressID as key_value,
# MAGIC         dbt_scd_id,
# MAGIC         dbt_valid_from as valid_from,
# MAGIC         dbt_valid_to as valid_to
# MAGIC     from `azureadb1`.`snapshots`.`address_snapshot`
# MAGIC ),
# MAGIC
# MAGIC pairs as (
# MAGIC     select
# MAGIC         a.key_value,
# MAGIC         a.valid_from,
# MAGIC         a.valid_to,
# MAGIC         b.valid_from as other_from,
# MAGIC         b.valid_to as other_to
# MAGIC     from scd a
# MAGIC     join scd b
# MAGIC         on a.key_value = b.key_value
# MAGIC         and a.valid_from < b.valid_to
# MAGIC         and b.valid_from < a.valid_to
# MAGIC         and a.dbt_scd_id <> b.dbt_scd_id
# MAGIC )
# MAGIC
# MAGIC select * from pairs
# MAGIC
# MAGIC
# MAGIC   
# MAGIC   
# MAGIC       
# MAGIC     ) dbt_internal_test

# COMMAND ----------

# MAGIC %sql
# MAGIC  select
# MAGIC         *
# MAGIC     from `azureadb1`.`snapshots`.`address_snapshot`
# MAGIC     where AddressID in(9,11)

# COMMAND ----------

# MAGIC %sql
# MAGIC update `azureadb1`.`snapshots`.`address_snapshot`  set dbt_valid_to=null where addressid in(9,11)

# COMMAND ----------

# MAGIC %sql
# MAGIC select now()

# COMMAND ----------

# MAGIC %sql
# MAGIC update  `azureadb1`.`saleslt`.`address` set AddressLine1 = "123 test address" where AddressID in(9,11)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from `azureadb1`.`snapshots`.`address_snapshot` where AddressID in(11,9)

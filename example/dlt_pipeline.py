# Databricks notebook source
import dlt
import sys
from pyspark.sql.functions import expr
import main

@dlt.view
def taxi_raw():
  return main.get_taxis()

@dlt.table
def filtered_taxis():
  return dlt.read("taxi_raw").filter(expr("fare_amount < 30"))
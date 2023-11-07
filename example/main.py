from pyspark.sql import SparkSession

def get_taxis():
  spark = SparkSession.builder.getOrCreate()
  return spark.read.table("samples.nyctaxi.trips")

def main():
  get_taxis().show(5)


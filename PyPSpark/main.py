from pyspark.sql import SparkSession
from pyspark import SparkConf

spark = (SparkSession.builder.appName("Datacamp Pyspark Tutorial")
         .config("spark.memory.offHeap.enabled", "true")
         .config("spark.memory.offHeap.size", "10g").getOrCreate())

spark.sparkContext.setLogLevel("INFO")

df = spark.read.csv('netflix_titles.csv', header=True, escape="\"")

df.show(5, 0)

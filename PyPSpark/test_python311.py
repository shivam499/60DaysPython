import os
import sys
import socket
print(f"Python Version: {sys.version}")

# Set environment variables before importing PySpark
os.environ['HADOOP_HOME'] = r"C:\winutils"
os.environ['SPARK_LOCAL_IP'] = "127.0.0.1"
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# Verify winutils setup
winutils_path = os.path.join(os.environ['HADOOP_HOME'], 'bin', 'winutils.exe')
hadoop_dll_path = os.path.join(os.environ['HADOOP_HOME'], 'bin', 'hadoop.dll')

print("\nChecking Hadoop binaries:")
print(f"Winutils path exists: {os.path.exists(winutils_path)}")
print(f"Hadoop DLL exists: {os.path.exists(hadoop_dll_path)}")

# Print environment information for debugging
print("\nEnvironment Variables:")
print(f"HADOOP_HOME: {os.environ.get('HADOOP_HOME')}")
print(f"PYSPARK_PYTHON: {os.environ.get('PYSPARK_PYTHON')}")
print(f"PYSPARK_DRIVER_PYTHON: {os.environ.get('PYSPARK_DRIVER_PYTHON')}")

from pyspark.sql import SparkSession
import logging

# Configure logging
logging.basicConfig(level=logging.WARN)
logger = logging.getLogger('pyspark')
logger.setLevel(logging.WARN)

# Initialize Spark Session with additional configurations
spark = SparkSession.builder \
    .appName("PySpark Test") \
    .config("spark.driver.host", "127.0.0.1") \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .config("spark.python.version", "3.11") \
    .config("spark.executor.instances", "1") \
    .config("spark.driver.memory", "1g") \
    .config("spark.executor.memory", "1g") \
    .config("spark.python.worker.reuse", "false") \
    .config("spark.network.timeout", "800s") \
    .config("spark.executor.heartbeatInterval", "60s") \
    .config("spark.logConf", "false") \
    .config("spark.ui.showConsoleProgress", "false") \
    .master("local[*]") \
    .getOrCreate()

# Set Spark log level
spark.sparkContext.setLogLevel("ERROR")

try:
    # Create a simple DataFrame
    data = [("John", 30), ("Alice", 25), ("Bob", 35)]
    df = spark.createDataFrame(data, ["Name", "Age"])

    # Show the DataFrame
    print("\nDataFrame Contents:")
    df.show()

    # Print versions
    print(f"\nPySpark Version: {spark.version}")
    print(f"Python Version in Spark: {spark.sparkContext.pythonVer}")
    print(f"Master: {spark.sparkContext.master}")

except Exception as e:
    print(f"\nError occurred: {str(e)}")
    import traceback
    traceback.print_exc()
finally:
    # Stop the Spark session
    if 'spark' in locals():
        spark.stop()

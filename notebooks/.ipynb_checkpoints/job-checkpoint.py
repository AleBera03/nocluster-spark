from pyspark import SparkConf, SparkContext
import findspark as fs
fs.init()

infilename = "example.txt"
inputpath = f"data/{infilename}"
outputpath = "output"

conf = SparkConf().setAppName("example")
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")

# program here

sc.stop()
Title: Hello PySpark World
Date: 2016-07-23
Modified: 2016-07-23
Category: Big Data
Tags: pyspark, spark, python
Slug: hello-pyspark-world
Disqus_identifier: hello-pyspark-world-4cebc7d3a90149dd9a18c71266a29e17
Summary: Develop Apache Spark applications using Python.
Status: draft

When learning [Apache Spark](http://spark.apache,org), the most common first example seems to be a program to count the number of words in a file. Let's see how we can write such a program using the [Python API](http://spark.apache.org/docs/latest/api/python/index.html) for Spark (PySpark).

In order to create standalone Python scripts using Visual Studio as your integrated development environment (IDE), check out the [post](pyspark-visual-studio.html) about installting Spark and setting up the IDE. 


[gist:id=57778e3f3f4d4ff4a8e49985ca4dce06]

```python hl_lines="1 3"
import operator
import pyspark

with pyspark.SparkContext("local", "HelloPySparkWorld") as sc:
    sc.filter
```

now explain what the code does in some detail.


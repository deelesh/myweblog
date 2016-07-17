Title: Hello PySpark World
Date: 2016-07-16
Modified: 2016-07-16
Category: Big Data
Tags: pyspark, spark, python
Slug: hello-pyspark-world
Disqus_identifier: hello-pyspark-world-4cebc7d3a90149dd9a18c71266a29e17
Summary: Writing Apache Spark applications using Python.
Status: published

When learning [Apache Spark](http://spark.apache,org), the most common first example seems to be a program to count the number of words in a file. Let's see how we can write such a program using the [Python API](http://spark.apache.org/docs/latest/api/python/index.html) for Spark (PySpark). This post assumes that you have already installed Spark. If you need a refresher on how to install Spark on Windows, checkout this [post](pyspark-windows.html).

[TOC]

## Word Count Program

In this post we will learn how to write a program that counts the number of words in a file. To achieve this, the program needs to read the entire file, split each line on space and count the frequency of each unique word. Since I did not want to include a special file whose words our program can count, I am counting the words in the same file that contains the source code of our program. The entire program is listed below

[gist:id=57778e3f3f4d4ff4a8e49985ca4dce06]

## Running Word Count Program

To run the Word Count program,

1. Open a terminal window such as a Windows Command Prompt.

2. Change into your SPARK_HOME directory.

3. Run the `spark-submit` utility and pass the full path to your Word Count program file as an argument.

For example, on my Windows laptop I used the following commands to run the Word Count program.

```
    cd %SPARK_HOME%
    bin\spark-submit c:\code\pyspark-hello-world.py
``` 

## Building Blocks of a PySpark Program

In order to understand how the Word Count program works, we need to first understand the basic building blocks of any PySpark program. A PySpark program can be written using the following workflow 

- Import the [pyspark](http://spark.apache.org/docs/latest/api/python/index.html) Python module.

- Create the [SparkContext](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkContext) by specifying the URL of the cluster on which to run your application and your application name.

- Use one or more methods of the `SparkContext` to create a [resilient distributed dataset](http://spark.apache.org/docs/latest/programming-guide.html#resilient-distributed-datasets-rdds) (RDD) from your big data.

- Apply one or more transformations on your RDDs to process your big data.

- Apply one or more actions on your RDDs to produce the outputs.    

## How the Word Count Program Works

Let's see how we apply the PySpark workflow in our Word Count program. We first import the `pyspark` module along with the [operator](http://docs.python.org/2/library/operator.html) module from the Python standard library as we need to later use the `add` function from the `operator` module.

    :::python
    import operator
    import pyspark

Once the `pyspark` module is imported, we create a `SparkContext` instance passing in the special keyword string, `local`, and the name of our application, `PySparkWordCount`. The `local` keyword tells Spark to run this program locally in the same process that is used to run our program. Realistically you will specify the URL of the Spark cluster on which your application should run and not use the `local` keyword. The `SparkContext` is created using the [with statement](http://docs.python.org/2/reference/compound_stmts.html#with) as the `SparkContext` needs to be closed when our program terminates.

    :::python
    with pyspark.SparkContext("local", "PySparkWordCount") as sc:
        #Get a RDD containing lines from this script file   

Using the [textFile](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkContext.textFile) method on the `SparkContext` instance, we get a RDD containing all the lines from the program file. The path to the program file is obtained using `__file__` name.

    :::python
    lines = sc.textFile(__file__)

We then apply two transformations to the `lines` RDD. First we split each line using a space to get a RDD of all words in every line using the [flatMap](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD.flatMap) transformation. Then we create a new RDD containing a list of  two value tuples where each tuple associates the number 1 with each word like `[(import 1), (operator, 1)]` using the [map](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD.map) transformation. 

    :::python
    words = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1))

Note the use of [lambda expression](http://docs.python.org/2/tutorial/controlflow.html#lambda-expressions) in the `flatMap` and `map` transformations. Lambda expressions are used in Python to create anonymous functions at runtime without binding the functions to names. The above line could also be written as

    :::python
    def split_line(line):
        return line.split(" ")

    def assign_one(word):
        return (word, 1)

    words = lines.flatMap(split_line).map(assign_one)
    
If you are not used to lambda expressions, defining functions and then passing in function names to Spark transformations might make your code easier to read. But the Spark documentation seems to use lambda expressions in all of the Python examples. So it is better to get used to lambda expressions.

>Lambda expressions can have only one statement which returns the value. In case you need to have multiple statements in your functions, you need to use the pattern of defining explicit functions and passing in their names.

We then apply the [reduceByKey](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD.reduceByKey) transformation to the `words` RDD passing in the `add` function from the `operator` standard library module. This creates a new RDD that is like a dictionary with keys as unique words in the file and values as the frequency of the words.

    :::python
    counts = words.reduceByKey(operator.add)

We then sort the `counts` RDD in the descending order based on the frequency of unique words such that words with highest frequency are listed first by applying the [sortyBy](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD.sortBy) transformation.

    :::python
    sorted_counts =  counts.sortBy(lambda x: x[1], False)

Finally we get an iterator over the `sorted_counts` RDD by applying the [toLocalIterator](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD.toLocalIterator) action to print each unique word in the file and its frequency. 

    :::python
    for word,count in sorted_counts.toLocalIterator():
        print(u"{} --> {}".format(word, count))

> We are using the `toLocalIterator` action instead of the [collect](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD.collect) action as `collect` will return the entire list in memory which might cause an out of memory error if the input file is really big. By using the `toLocalIterator` action, our program will only hold a single word in memory at any time.

## Summary

You can write PySpark programs by creating a `SparkContext`, loading your big data as an RDD, applying one or more transformations to the RDDs to perform your processing and applying one or more actions to the processed RDDs to get the results.


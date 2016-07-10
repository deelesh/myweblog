# MyWeblog

This repository stores the content as well as the Python code used to generate my weblog http://deelesh.github.io. 

The weblog is generated using [Pelican](http://getpelican.com).

## Install Instructions

Follow these steps to setup a machine with pelican and all the necessary pelican themes and plugins. The commands need to be executed in an active Python virtual environment.

1. Setup a Python 2.7 virtual environment and activate it.

2. Install the required packages in the virtual environment.

 ```
     pip install -r requirements.txt
 ```

3. Install pelican themes

```
    git clone --recursive https://github.com/getpelican/pelican-themes
```

4. Install pelican plugins

```
    git clone --recursive https://github.com/getpelican/pelican-plugins
``` 

## Publishing the Weblog

In order to publish the weblog, the following commands need to be executed in an active virtual environment.

- To build the dev version of the weblog 

    ```
        pelican content
    ```

- To preview the weblog on http://localhost:8000 

    ```
        cd output
        python -m pelican.server
    ``` 

- To publish the weblog as user pages on Github

    ```
        pelican content -s publishconf.py -o output
    ```
    and push the contents of the output folder to the master branch of deelesh.github.io repo
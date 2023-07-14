# Semantic similarities

This small application uses NLP to find similarities in text

## Table of Contents
- [Running the project](#installation)
- [Using Docker](#using-docker)

## Installation
To run Semantic similarity follow these steps:

1. Clone the repository:

   [Repo](https://github.com/kudzaizvov/nlp-semantic-similarity.git)

2.  Navigate to the project directory:
3. Install the dependencies:
   * Create a Virtual env
      * python3 -m venv env   
      * source env/bin/activate
   * run `pip install -r /path/to/requirements.txt`
    
4. run `python semantic.py`
  

## Using Docker
You can build a docker image using the following commands

1. `docker build -t <docker-tag> .`
2. `docker run <docker-tag>`

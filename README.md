# Todo Application

This README describes the steps to get your Todo application up and running.

## Prerequisites

Make sure you have Docker and Python installed on your system.

## Set Up

Follow the steps below to get your application running:

### Setting Up The Virtual Environment

1. We're using a virtual environment. Activate it using: `source .venv/bin/activate`
2. Install the necessary Python packages: `pip install psycopg2-binary`

### Setting Up Docker

1. Build Docker using the following command: `docker-compose up`

### Setting Up Database 

1. We're using Django's built-in database management commands. Run the migrations using: `python3 manage.py makemigrations && python3 manage.py migrate`

At this point, your application should be up and running.
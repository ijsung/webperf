# Webperf: a performance visualization tool

## What is this

Webperf is a simple web application that renders a time series of performance
measurements and render it using MetricGraphics. It contains a
static frontend, and a backend (based on Django REST framework)
that runs on your localhost.

# Installation

Because the frontend is static, we host it on Github Pages. We do
still need you to install the backend on your local machine.

This document contains current recommended steps required to try
out the performance visualization backend which is still WIP. After
following the steps, you would have the backend up and running on
localhost at port 8000 rendering one benchmark. This backend can
be accessed by either the API interface directly (shown later), or
via a visualization frontend currently hosted on Github Pages
(http://ijsung.github.io/webperf)


There is strictly no security means set up yet, so you should make
sure your local machine is well isolated behind a firewall from the
Internet.


This tutorial has been verified on an OS X El Capitan machine, but
should work with systems that Python, Django and SQLite run on.

## Prerequisites
* Python 2.7 for backend
* Python 2/3 for uploading script
* Install pip
* Install virtualenv via pip

```
pip install virtualenv
```	

There are multiple ways of doing so, and what I tried was installing
a slightly newer Python and pip both from homebrew.  

## Checkout the web-backend code

```
git clone https://github.com/ijsung/webperf.git
```

### Setup python packages needed, inside virtualenv

```
cd webperf
# Create a virtualenv to isolate our package dependencies locally
virtualenv env
source env/bin/activate  # On Windows use `env\Scripts\activate`


# Install Django and Django REST framework into the virtualenv
pip install django
pip install djangorestframework
# Install CORS headers so that we can request JSON from the frontend on a different machine
pip install django-cors-headers
```	



### Migrate or initialize the database
```
# Need these two commands when there’s any change to Models
python manage.py makemigrations backend
python manage.py migrate
```	

### Perform regression tests (optional)

```
python manage.py test
# the following steps require “pip install coverage==3.6” in the virtualenv
coverage run manage.py test -v 2 # optional. run coverage testing
coverage html #optional. generate coverage report in HTML
```	

### Run server locally at 127.0.0.1:8000
```
python manage.py runserver
```	

### Add benchmark, measurements, and visualize the results

#### Add a benchmark

Open your browser, go to http://localhost:8000/benchmarks/ and add
at least one benchmark. The frontend now displays results with a
benchmark name of your choice.

#### Add a measurement data point
Open your browser, go to http://localhost:8000/measurements/ and
add a few entries via the form below with the benchmark added in
previous step.


  

#### Try out the visualization frontend.

Go to http://ijsung.github.io/webperf/ and click the “All Results”.
You should see the numbers you just added shown there in the chart.

  



This accesses the database we just created via JSON and renders it as a time series in your browser.

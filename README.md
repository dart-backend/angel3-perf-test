# angel3-perf-test

This repository contains the code for running performance tests on Angel3 framework using Locust framework

## Software Requirements

* Python: 3.13.x

## Installation

Setup the environment for development and executing the load tests

1. Run the following commands

    ```bash
        python -m venv venv
        ./venv/Scripts/activate
        pip install -r requirements.txt
    ```

## Running the load tests

1. Run the following command to enable the local python environment

    ```bash
        ./venv/Scripts/activate
    ```

2. Run the test cases

    ```bash
        locust -f tests_suite/load_tests/001_test.py --host http://localhost:8080
    ```

3. Open the link in the browser

# Angel3 framework performance tests

This repository contains the code for running performance tests on Angel3 framework using Locust framework

## Software Requirements

* Python: 3.13.x

## Installation

Setup the environment for development and executing the load tests

1. Run the following commands

    ```bash
        python3 -m venv venv
        source ./venv/bin/activate
        pip install -r requirements.txt
    ```

## Running the load tests

1. Run the following command to enable the local python environment

    ```bash
        ./venv/bin/activate
    ```

2. Launch the Locust load test server

    ```bash
        locust -f tests_suite/load_tests/000_template.py --host http://localhost:8080
    ```

3. Open the provided link in the browser to run the load tests

# cross-dag-dependencies-tutorial
This repo contains examples to implement cross-DAG dependencies in your Airflow DAGs. A guide with an in-depth explanation of how to implement cross-DAG dependencies can be found [here](https://www.astronomer.io/guides/cross-dag-dependencies).

There are multiple ways of achieving cross-DAG dependencies in Airflow, which are each represented by an example DAG in this repo. These methods include:

 - Using the `TriggerDagRunOperator`, as highlighted in `trigger-dagrun-dag.py`
 - Using the `ExternalTaskSensor`, as highlighted in `external-task-sensor-dag.py`
 - Using the Airflow API (for Airflow 2.0 or greater), as highlighted in `api-dag.py`
 
All of these examples should work out of the box if you are running Airflow 2.0 or greater (this repo runs Airlfow 2.1 using the Astronomer CLI). Note that to run the API example, you will need to set up a connection (more on this in the guide linked above)

## Getting Started
The easiest way to run these example DAGs is to use the Astronomer CLI to get an Airflow instance up and running locally:

 1. [Install the Astronomer CLI](https://www.astronomer.io/docs/cloud/stable/develop/cli-quickstart)
 2. Clone this repo somewhere locally and navigate to it in your terminal
 3. Initialize an Astronomer project by running `astro dev init`
 4. Start Airflow locally by running `astro dev start`
 5. Navigate to localhost:8080 in your browser and you should see the tutorial DAGs there

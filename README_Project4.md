
# Project 4: Real-Time Data Processing with Kafka and MongoDB

## Project Description

The objective of this project is to simulate real-time data processing using **Kafka**. Additionally, this project integrates two types of databases: **MongoDB** and **PostgreSQL**. The dataset consists of two CSV files:

1. **Old_Information.csv** – This file contains historical transaction data, which is stored in PostgreSQL.
2. **New_Information.csv** – This file represents new transaction data simulated through Kafka as a message broker.

The new transactions from `New_Information.csv` are produced by Kafka, then consumed and merged with the old transactions from `Old_Information.csv`. A machine learning model is used to predict whether each transaction is fraudulent or not.

---

## About the Dataset

- **Old_Information.csv**: Contains historical transaction data.
- **New_Information.csv**: Simulated new transaction data produced by Kafka.
- Both datasets contain details such as origin and destination account names.

---

## Tools and Technologies

The following tools were used in this project:

- **PostgreSQL** – For storing historical transaction data.
- **Kafka** – For simulating real-time data streaming.
- **MongoDB** – For storing the merged data and prediction results.
- **Docker** – For containerizing the services required in the project.

---

## Workflow & Results

To execute the entire workflow, follow the steps outlined below:

1. Run `docker-compose` to install the necessary tools (PostgreSQL, Kafka, MongoDB).
2. Ingest the historical data into PostgreSQL by running the `dump_to_database.py` script.
3. Simulate the producer in Kafka using the new data (`New_Information.csv`) by creating a Kafka producer.
4. Load the pre-trained machine learning model and establish a connection to MongoDB.
5. Join the old and new transaction data on the columns `'nameOrig'` and `'nameDest'`.
6. Run predictions using the machine learning model (`FraudModel.py`) to classify transactions as fraudulent or not.
7. Store the merged data and predictions into MongoDB under the collection `mongo-project4`, and save the results in a CSV file located at `data_final/ftde02.mongo-project4.csv`.

---

## Future Improvements

- Implement a **timeout** for both Kafka producer and consumer processes to avoid manual interruptions.
- Explore additional Kafka functionalities that allow the program to stop once all data has been produced or consumed successfully (i.e., after the last message has been processed).


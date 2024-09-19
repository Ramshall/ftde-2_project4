import json
import pandas as pd
from kafka import KafkaProducer
import time

if __name__ == "__main__":

    # Use a relative path to the CSV file
    data = pd.read_csv('./data/New_Information.csv')
    json_data = data.to_dict(orient='records')

    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    count = 0  # Counter to track how many records are produced

    for record in json_data:
        producer.send("ftde02-project4", record)
        count += 1  # Increment counter for each record produced
        print(f"Produced record {count}: {record}")
        time.sleep(1)  # Optional delay between sending records

    # Ensure all messages are sent and close the producer
    producer.flush()
    producer.close()
    
    # Print the total number of records produced
    print(f"Producer selesai mengirim {count} record(s).")

import pandas as pd
import urllib.parse
from sqlalchemy import create_engine

def insert_data_to_postgresql(df, table_name, db_url):
    try:
        engine = create_engine(db_url)

        # Insert data into PostgreSQL
        df.to_sql(table_name, engine, if_exists='append', index=False)
        print(f"Data telah dimasukkan ke tabel {table_name}.")
    except Exception as e:
        print(f"Terjadi kesalahan saat memasukkan data: {e}")
    finally:
        # Close the engine connection
        engine.dispose()

if __name__ == "__main__":
    csv_path = ".\\data\\Old_Information.csv"
    data = pd.read_csv(csv_path)
    
    # Informasi koneksi ke PostgreSQL
    username = "postgres"
    password = "postgres"
    host = "localhost"
    port = "5432"
    database = "data_project_4"
    password = urllib.parse.quote_plus(password)

    # URL koneksi ke PostgreSQL
    db_url = f"postgresql://{username}:{password}@{host}:{port}/{database}"

    table_name = "old_information"
    
    # Insert data into PostgreSQL
    insert_data_to_postgresql(data, table_name, db_url)
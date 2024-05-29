import configparser
import pandas as pd
from sqlalchemy import create_engine

config = configparser.ConfigParser()
config.read('config.ini')

username = config.get('postgres', 'username')
password = config.get('postgres' 'password')
host = config.get('postgres', 'host')
port = config.get('postgres', 'port')

def create_db_and_tables():
    engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/ecommerce')

    # Read CSV files
    customers = pd.read_csv('data/customers.csv')
    orders = pd.read_csv('data/orders.csv')
    products = pd.read_csv('data/products.csv')

    # Create tables and insert data
    customers.to_sql('customers', engine, index=False, if_exists='replace')
    orders.to_sql('orders', engine, index=False, if_exists='replace')
    products.to_sql('products', engine, index=False, if_exists='replace')

if __name__ == '__main__':
    create_db_and_tables()

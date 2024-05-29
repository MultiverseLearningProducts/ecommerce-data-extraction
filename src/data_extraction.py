import configparser
from sqlalchemy import create_engine, text

config = configparser.ConfigParser()
config.read('config.ini')

username = config.get('postgres', 'username')
password = config.get('postgres' 'password')
host = config.get('postgres', 'host')
port = config.get('postgres', 'port')

def extract_and_join_data():
    engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/ecommerce')
    with engine.connect() as connection:
        result = connection.execute(text("""
            SELECT c.first_name as customer_name, p.product_name, o.quantity, o.price, o.order_date
            FROM orders o
            JOIN customers c ON o.customer_id = c.customer_id
            JOIN products p ON o.product_id = p.product_id
        """))
        data = result.fetchall()
        return data

if __name__ == '__main__':
    data = extract_and_join_data()
    for row in data:
        print(row)

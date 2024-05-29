import pandas as pd
from data_extraction import extract_and_join_data

def export_to_csv(data):
    df = pd.DataFrame(data, columns=['customer_name', 'product_name', 'quantity', 'price', 'order_date'])
    df.to_csv('data/joined_data.csv', index=False)

if __name__ == '__main__':
    data = extract_and_join_data()
    export_to_csv(data)

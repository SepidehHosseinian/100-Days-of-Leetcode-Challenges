import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # Group by customer_number and count the number of orders for each customer
    customer_order_counts = orders.groupby('customer_number')['order_number'].count().reset_index()
    
    # Find the customer with the largest number of orders
    max_orders_customer = customer_order_counts[customer_order_counts['order_number'] == customer_order_counts['order_number'].max()][['customer_number']]
    
    return max_orders_customer
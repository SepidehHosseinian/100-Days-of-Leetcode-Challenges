import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
     # Calculate the count of immediate orders
    immediate_count = delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']].shape[0]
    
    # Calculate the total count of orders
    total_orders = delivery.shape[0]
    
    # Calculate the percentage of immediate orders
    immediate_percentage = (immediate_count / total_orders) * 100
    
    # Create a DataFrame to store the result
    result_df = pd.DataFrame({'immediate_percentage': [round(immediate_percentage, 2)]})
    
    return result_df
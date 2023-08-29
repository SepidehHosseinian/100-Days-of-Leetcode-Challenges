import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Merge SalesPerson, Orders, and Company tables
    merged_data = sales_person.merge(orders, on='sales_id', how='left').merge(company, on='com_id', how='left')
    
    # Filter rows where the company name is not "RED" or is null
    filtered_data = merged_data[(merged_data['name_y'] != 'RED') | (merged_data['name_y'].isna())]
    
    # Select the 'name_x' column, which represents the salesperson's name
    result = filtered_data[['name_x']].rename(columns={'name_x': 'name'})
    
    # Drop duplicates (in case a salesperson had multiple orders not related to "RED")
    result = result.drop_duplicates()
    
    # Find the salespersons who had orders related to "RED"
    sales_with_red_orders = merged_data[merged_data['name_y'] == 'RED']['name_x'].unique()
    
    # Filter out salespersons with "RED" orders from the result
    result = result[~result['name'].isin(sales_with_red_orders)]
    
    return result
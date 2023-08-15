import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # Create an empty list to store the rearranged rows
    rearranged_rows = []

    # Iterate over each row in the original table
    for _, row in products.iterrows():
        product_id = row['product_id']

        # Check each store for price availability
        for store_col in ['store1', 'store2', 'store3']:
            price = row[store_col]
            if pd.notna(price):
                # If the price is not null, add the (product_id, store, price) tuple to the list
                rearranged_rows.append((product_id, store_col, price))

    # Create a new DataFrame with the rearranged rows
    result_table = pd.DataFrame(rearranged_rows, columns=['product_id', 'store', 'price'])

    return result_table
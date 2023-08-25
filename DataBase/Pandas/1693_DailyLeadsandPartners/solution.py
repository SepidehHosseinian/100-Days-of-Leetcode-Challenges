import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    # Group the daily sales by date_id and make_name, and count distinct lead_id's and partner_id's
    grouped = daily_sales.groupby(['date_id', 'make_name']).agg({'lead_id': 'nunique', 'partner_id': 'nunique'}).reset_index()
    
    # Rename the columns for clarity
    grouped.columns = ['date_id', 'make_name', 'unique_leads', 'unique_partners']
    
    return grouped
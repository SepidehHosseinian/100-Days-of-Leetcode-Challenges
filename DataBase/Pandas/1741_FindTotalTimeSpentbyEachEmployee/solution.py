import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    # Calculate the time spent for each entry
    employees['time_spent'] = employees['out_time'] - employees['in_time']
    
    # Group by emp_id and event_day, then sum the time_spent
    result = employees.groupby(['emp_id', 'event_day'])['time_spent'].sum().reset_index()
    result.rename(columns={'event_day': 'day', 'time_spent': 'total_time'}, inplace=True)
    
    return result
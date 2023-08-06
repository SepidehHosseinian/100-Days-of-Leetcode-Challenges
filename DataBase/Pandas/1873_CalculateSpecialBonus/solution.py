import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Create a new column 'bonus' with default value 0
    employees['bonus'] = 0
    
    # Calculate bonus based on the conditions
    employees.loc[(employees['employee_id'] % 2 != 0) & (~employees['name'].str.startswith('M')), 'bonus'] = employees['salary']
    
    # Select only the required columns and sort the result table by employee_id in ascending order
    result_df = employees[['employee_id', 'bonus']].sort_values(by='employee_id', ascending=True)
    
    return result_df
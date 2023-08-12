import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    if employee.empty or department.empty:
        return pd.DataFrame(columns=['Department','Employee', 'Salary'])
    
    # Merge the employee and department DataFrames on 'departmentId' and 'id' columns
    merged_df = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_employee', '_department'))
    
    # Use groupby to group data by 'departmentId' and apply a lambda function to get employees with highest salary in each group
    highest_salary_df = merged_df.groupby('departmentId').apply(lambda x: x[x['salary'] == x['salary'].max()])
    
    # Drop the duplicate 'departmentId' column and reset the index
    highest_salary_df = highest_salary_df.reset_index(drop=True)
    
    # Select the required columns and return the result
    result_df = highest_salary_df[['name_department', 'name_employee', 'salary']]
    
    # Rename the columns as specified
    result_df.columns = ['Department','Employee', 'Salary']
    
    return result_df
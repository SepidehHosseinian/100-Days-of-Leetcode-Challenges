import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    # Drop any duplicate salary values to avoid counting duplicates as separate salary ranks
    unique_salaries = employee['salary'].drop_duplicates()

    # Sort the unique salaries in descending order and get the Nth highest salary
    sorted_salaries = unique_salaries.sort_values(ascending=False)

    # If N exceeds the number of unique salaries, return None
    if N > len(sorted_salaries):
        return pd.DataFrame({'Nth Highest Salary': [None]})
    
    # Get the Nth highest salary from the sorted salaries
    nth_highest = sorted_salaries.iloc[N - 1]
    
    return pd.DataFrame({'Nth Highest Salary': [nth_highest]})
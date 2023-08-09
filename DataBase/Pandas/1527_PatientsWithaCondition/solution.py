import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # Use the str.contains() method to find patients with Type I Diabetes
    patients_with_diabetes = patients[patients['conditions'].str.contains(r'\bDIAB1')]
    
    # Select only the required columns
    result_df = patients_with_diabetes[['patient_id', 'patient_name', 'conditions']]
    
    return result_df
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # Group by class and count the number of students in each class
    class_counts = courses.groupby('class')['student'].count().reset_index()
    
    # Filter classes with at least five students
    result = class_counts[class_counts['student'] >= 5][["class"]]
    
    return result
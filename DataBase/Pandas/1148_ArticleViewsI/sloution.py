import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
     # Filter and select the 'author_id' column for authors who viewed their own articles
    result_df = views[views['author_id'] == views['viewer_id']][['author_id']]
    
    # Sort the result by 'author_id' in ascending order and remove duplicates
    result_df = result_df.sort_values('author_id').drop_duplicates()
    result_df.columns = ["id"]
    return result_df
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    stats = actor_director.groupby(
        ['actor_id', 'director_id'],
    ).agg(
        count=('director_id', 'count'),
    ).reset_index()
    return stats[stats['count'] >= 3][['actor_id', 'director_id']]
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicates = person[person.duplicated(subset=['email'])]

    return duplicates[['email']].drop_duplicates()
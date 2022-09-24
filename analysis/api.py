def sort_by_field_ascending(df: list, field: str) -> list:
    """Sorts a dataframe based on a numerical field"""
    return sorted(df, key=lambda row: float(row[field]))

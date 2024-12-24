import polars as pl

def extract_parquet(file_path):
    """
    Reads a Parquet file and returns a Polars DataFrame.
    """
    try:
        df = pl.read_parquet(file_path)
        return df
    except Exception as e:
        print(f"Error reading Parquet file: {e}")
        return None

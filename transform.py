import pandas as pd
import logging

def transform_data(raw_data: list[dict]) -> pd.DataFrame:
    """Transform raw API data to count words in each post"""
    logging.info("Starting data transformation")
    
    try:
        # Convert to DataFrame
        df = pd.DataFrame(raw_data)
        
        # Count words in title and body
        df['body_word_count'] = df['body'].str.split().str.len()
        
        
        logging.info("Data transformation completed successfully")
        return df
    except Exception as e:
        logging.error(f"Error during data transformation: {str(e)}")
        raise

if __name__ == "__main__":
    from extract import fetch_data
    data = fetch_data()
    transformed = transform_data(data)
    print(transformed.head())
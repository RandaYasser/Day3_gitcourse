import pandas as pd
import logging
from datetime import datetime

def save_to_csv(data: pd.DataFrame, filename: str = None) -> str:
    """Save transformed data to CSV file"""
    try:
        if not filename:
            filename = f"output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        logging.info(f"Saving data to {filename}")
        data.to_csv(filename, index=False)
        logging.info(f"Data successfully saved to {filename}")
        return filename
    except Exception as e:
        logging.error(f"Error saving data to CSV: {str(e)}")
        raise

if __name__ == "__main__":
    from transform import transform_data
    from extract import fetch_data
    
    data = fetch_data()
    transformed = transform_data(data)
    save_to_csv(transformed)
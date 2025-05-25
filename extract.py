import requests
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('etl_pipeline.log'),
        logging.StreamHandler()
    ]
)

def fetch_data(api_url: str = "https://jsonplaceholder.typicode.com/posts") -> list[dict]:
    """Extract data from API and return as JSON"""
    try:
        logging.info(f"Extracting data from {api_url}")
        response = requests.get(api_url, timeout=10)
        logging.info("Data extraction successful")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error during data extraction: {str(e)}")
        raise

if __name__ == "__main__":
    data = fetch_data()
    print(f"Extracted {len(data)} records")
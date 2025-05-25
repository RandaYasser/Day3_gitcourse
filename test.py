import requests
import logging
from transform import transform_data
import pytest
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_api_response():

    logger.info("Testing API response...")
    response = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=10)
    assert response.status_code == 200, f"Bad status code: {response.status_code}"
    logger.info("API test passed (status 200 with data)")


def test_word_count_calculation():
    """Test that word counts are calculated correctly"""
    sample_data = [
        {"userId": 1, "id": 1, "title": "Simple title", "body": "This is a test body."}
    ]
    result = transform_data(sample_data)
    
    # Check the structure of the returned DataFrame
    assert set(result.columns) == {'userId', 'id', 'title', 'body', 'body_word_count'}

    # Test specific word counts
    assert result.loc[0, 'body_word_count'] == 5    # "This is a test body."


def test_empty_input():
    """Test handling of empty input"""
    with pytest.raises(Exception):
        transform_data([])

def test_missing_fields():
    """Test handling of missing required fields"""
    with pytest.raises(Exception):
        transform_data([{"userId": 1}])  # Missing title and body

if __name__ == "__main__":
    logger.info("Running tests...")
    pytest.main([__file__])
    logger.info("Tests completed.")
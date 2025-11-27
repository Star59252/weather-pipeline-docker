import unittest
from weather_etl import transform

class TestWeatherETL(unittest.TestCase):
    
    def test_transform_data(self):
        # 1. Simulate fake data from OpenWeatherMap
        mock_api_response = {
            "name": "Test City",
            "main": {
                "temp": 25.5,
                "humidity": 60,
                "pressure": 1013
            },
            "wind": {
                "speed": 5.2
            },
            "weather": [
                {"description": "clear sky"}
            ]
        }

        # 2. Run your transform function
        result = transform(mock_api_response)

        # 3. Check if the output matches what we expect
        self.assertEqual(result["city"], "Test City")
        self.assertEqual(result["temp"], 25.5)
        self.assertEqual(result["humidity"], 60)
        self.assertEqual(result["desc"], "clear sky")

if __name__ == '__main__':
    unittest.main()
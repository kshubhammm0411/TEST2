import unittest
import requests

class TestNotification(unittest.TestCase):
    def test_notification(self):
        # Set up the test parameters
        url = 'https://5aukw37tg9.execute-api.ap-south-1.amazonaws.com/default/slackNotification'
        params = {'channel_name': 'test', 'message': 'test lambda 2'}
        
        # Send the request and get the response
        resp = requests.post(url, params=params)
        
        # Verify that the request was successful
        self.assertEqual(resp.status_code, 200)
        
        # Verify that the response contains the expected message
        self.assertIn('Hello from lambda', resp.text)

# Run the testcd
if __name__ == '__main__':
    unittest.main()
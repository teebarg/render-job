import requests
import time
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

def api_call():
    try:
        response = requests.get('https://template-api.niyi.com.ng/api/health-check')
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error making API call: {str(e)}")
        return None

def main():
    logging.info("Starting the application")
    while True:
        try:
            response_text = api_call()
            if response_text:
                logging.info(f"API Response: {response_text}")
                print('\n\n\n')
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")

        time.sleep(60*5)  # Sleep for 5 minutes

if __name__ == "__main__":
    main()

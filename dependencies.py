import requests
import logging
import sys

from contextlib import asynccontextmanager
import asyncio

from fastapi import FastAPI
from config import SETTINGS

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)


def api_call(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error making API call: {str(e)}")
        return None


async def refresh_endpoint():
    while True:
        try:
            for url in SETTINGS.URLs:
                if response_text := api_call(url=url):
                    logging.info(f"API Response from: {response_text}")
                    print('\n\n\n')
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
        await asyncio.sleep(600)


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(refresh_endpoint())
    yield

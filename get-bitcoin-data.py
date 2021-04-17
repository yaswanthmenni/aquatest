import requests
import json
import logging
import time
from datetime import datetime

bitcoin_api_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
logger_file_name = 'bitcoin_details.log'

logger = logging.getLogger('bitcoin')

def get_bitcoin_details():
    try:
        response = requests.get(bitcoin_api_url)
        date = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
        price = response.json()['bpi']['USD']['rate']
        message = "Bitcoin price is {0} at {1}".format(str(price), date)
        
        return message

    except Exception as err:
        logging.error("Got exception while fetching bitcoin data. Error: " + str(err))

def configLogger():
    logging.basicConfig(filename=logger_file_name, filemode='a', format='%(message)s',level=logging.INFO)

if __name__ == '__main__':
    try:
        print("Application started!")
        configLogger()
        while True:
            logger.info(get_bitcoin_details())
    except Exception as err:
        print("Got exception: " + str(err))
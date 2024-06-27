import pandas as pd

def read_data(data_path):
    return pd.read_csv(data_path)

import logging
logger = logging.getLogger('simple_logger')
logger.setLevel(logging.DEBUG)
fhandler = logging.FileHandler(filename='run.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s: %(lineno)d (%(funcName)s) %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)

logger.info("Info test")
logger.debug('Debug test')
logger.error('Error test')
# logging.info("Info test")
# logging.debug('Debug test')
# logging.error('Error test')
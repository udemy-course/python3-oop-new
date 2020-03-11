"""
debug()，info()，warning()，error()，critical()
"""
import logging

logging.basicConfig(level='INFO', filename='test.log', filemode='w')
logging.debug('this is debug')
logging.info('this is info')
logging.warning('this is warning')
logging.error('this is erro')
logging.critical('this is critical')

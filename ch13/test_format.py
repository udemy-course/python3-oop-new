"""
https://docs.python.org/3/library/logging.html#logrecord-attributes

"""
import logging

format = '%(asctime)s-%(funcName)s-%(lineno)d-%(levelname)s %(name)s %(message)s'

logging.basicConfig(level='INFO', format=format)
# logging.BASIC_FORMAT

def main():
    logging.debug('this is debug')
    logging.info('this is info')
    logging.warning('this is warning')
    logging.error('this is erro')
    logging.critical('this is critical')

if __name__ == "__main__":
    main()
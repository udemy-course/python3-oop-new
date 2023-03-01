import logging
from logging.config import fileConfig

fileConfig('log.conf')
logger = logging.getLogger()
logger.debug('often makes a very good meal of %s', 'visiting tourists')

# you will see the following output:
# DEBUG:root:often makes a very good meal of visiting tourists
# and log file will be created in the current directory called example.log

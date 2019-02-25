import logging

LOG_FILENAME = 'log.txt'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG,)
logging.debug('This message should go to the log file.')
with open(LOG_FILENAME, 'rt') as f:
	prg = f.read()
print('FILE:')
print(prg)

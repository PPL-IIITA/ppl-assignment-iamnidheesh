import logging

def logger(write) :
	logging.basicConfig(filename='q1.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
	logging.info(write)
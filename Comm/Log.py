import os
import logging
from logging.handlers import TimedRotatingFileHandler
from Conf.config import log_cfg

BaseHome = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

log_level = eval(log_cfg['log_level'])
log_path = log_cfg['log_path']
log_format = log_cfg['log_format']

log_file = os.path.join(BaseHome, log_path, 'log.txt')


def log_init():
    logger = logging.getLogger('main')
    logger.setLevel(level=log_level)
    formatter = logging.Formatter(log_format)

    handler = TimedRotatingFileHandler(filename=log_file, when='D', interval=1, backupCount=7)
    handler.setLevel(log_level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    console = logging.StreamHandler()
    console.setLevel(log_level)
    console.setFormatter(formatter)
    logger.addHandler(console)



log_init()
logger = logging.getLogger('main')
logger.debug('log test1....')
logger.info('log test2....')
logger.warning('log test3....')
logger.error('log test4....')
logger.critical('log test5....')

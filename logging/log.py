#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.config

# logging.basicConfig(level=logging.INFO,
#                     format='%(message)s',
#                     filename='myapp.log',
#                     filemode='a')

logging.config.fileConfig('logger.conf')
logger = logging.getLogger('root')

logger.info('test1')
logger.info('%test2%')
logger.debug('$test3$')
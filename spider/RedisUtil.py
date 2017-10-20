#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis

def getredis():
    pool = redis.ConnectionPool(host='10.10.6.181', password='cXkto.LF', port=6379)
    r = redis.Redis(connection_pool=pool)
    return r

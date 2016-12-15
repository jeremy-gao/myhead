#!/usr/bin/env python
#-*-coding:utf-8-*-

import os, bottle, sys
sys.path = ['/home/myhead/'] + sys.path
os.chdir(os.path.dirname(__file__))
import index
application = bottle.default_app()

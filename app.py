#!/usr/local/bin/python2.7
#coding:utf-8

import os
import sys
import traceback
from django.core.handlers.wsgi import WSGIHandler
from django.core.signals import got_request_exception
from django.core.management import call_command

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'jihua'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'jihua.settings'

def exception_printer(sender, **kwargs):
    traceback.print_exc()

got_request_exception.connect(exception_printer)
call_command('syncdb')
app = WSGIHandler()


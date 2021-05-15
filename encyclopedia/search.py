import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wiki.settings')
django.setup()

from encyclopedia.util import list_entries
import re
from encyclopedia import util
import django
from . import views
from django.http import request
a=[]
def search(keyword):    
    result = []

    i = 0
    l = util.list_entries()
    for x in l:
        if keyword.lower() == l[i].lower():
            return ("test_ok",l[i])
        elif keyword.lower() in l[i].lower():
            result.append(l[i])
            i += 1
        else:
            i += 1    
    a=result
    return a


        






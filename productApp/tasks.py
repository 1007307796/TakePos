from __future__ import absolute_import,unicode_literals
from celery import shared_task
from pyscript.file_handler import file_storage
from os import path
import json
from userApp.models import UserOrder 

@shared_task
def send_yzw_handler(code,oid):
    user_order = UserOrder.objects.get(pk=oid)
    suffix = user_order.user.username + '_' + str(user_order.id) + '.py'
    prefix = path.join(path.dirname(__file__),'backup')
    backup_path = file_storage(prefix,suffix)
    print(backup_path)
    with open(backup_path,'w+',encoding='utf-8') as f:
        f.write(code)
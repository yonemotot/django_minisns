# モジュールをimport
from django.contrib import admin
from .models import Message,Friend,Group,Good

# モデルを管理者サイトに登録
admin.site.register(Message)
admin.site.register(Friend)
admin.site.register(Group)
admin.site.register(Good)

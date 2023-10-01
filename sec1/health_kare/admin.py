from django.contrib import admin

# Register your models here.

from .models import pat_desc,doc_desc,user_input
admin.site.register(pat_desc)
admin.site.register(doc_desc)
admin.site.register(user_input)
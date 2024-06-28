from django.contrib import admin
from promise.models import Promise, BrokenPromise


admin.site.register(Promise)
admin.site.register(BrokenPromise)



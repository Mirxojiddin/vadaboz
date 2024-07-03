from django.contrib import admin
from promise.models import Promise, BrokenPromise,DislikeToPromise,LikeToPromise, PromiseCommit


admin.site.register(Promise)
admin.site.register(BrokenPromise)
admin.site.register(DislikeToPromise)
admin.site.register(LikeToPromise)
admin.site.register(PromiseCommit)




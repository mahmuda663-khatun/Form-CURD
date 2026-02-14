from django.contrib import admin
from myapp.models import*
# Register your models here.
admin.site.register(UserModel)
admin.site.register(ProfileModel)
admin.site.register(JobModel)
admin.site.register(ApplicationModel)
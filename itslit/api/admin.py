from django.contrib import admin
from .models import Photos, Offer, Biz, Hobby, UserProfile
# Register your models here.
admin.site.register(Photos)
admin.site.register(Offer)
admin.site.register(Biz)
admin.site.register(Hobby)
admin.site.register(UserProfile)

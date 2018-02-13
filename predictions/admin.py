from django.contrib import admin
from .models import Prediction, Stock, User, UserStock

# Register your models here.
admin.site.register(Prediction)
admin.site.register(Stock)
admin.site.register(User)
admin.site.register(UserStock)

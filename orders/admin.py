from django.contrib import admin

from .models import Matching, MatchingParticipant, OrderList, Restaurant, Menu

admin.site.register(Matching)
admin.site.register(MatchingParticipant)
admin.site.register(OrderList)
admin.site.register(Restaurant)
admin.site.register(Menu)

# Register your models here.

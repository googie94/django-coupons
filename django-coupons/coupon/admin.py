from django.contrib import admin

from .models import Coupon, CouponUser, Campaign

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
	list_display = ['id']

@admin.register(CouponUser)
class CouponUserAdmin(admin.ModelAdmin):
	list_display = ['id']

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
	list_display = ['id']

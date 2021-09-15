from .models import Coupon, CouponUser
from django.utils import timezone


class CouponSystem():

	def coupon_use(self, coupon_id):
		now = timezone.now()
		couponuser = CouponUser.objects.get(pk=coupon_id)
		couponuser.used_at = now
		couponuser.save()

	def coupon_return(self, coupon_id):
		couponuser = CouponUser.objects.get(pk=coupon_id)
		couponuser.used_at = None
		couponuser.save()
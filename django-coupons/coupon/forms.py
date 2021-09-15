from django import forms

from .models import Coupon, CouponUser

class CouponForm(forms.ModelForm):

	class Meta:
		model = Coupon
		fields = '__all__'


class CouponUserForm(forms.ModelForm):

	class Meta:
		model = CouponUser
		fields = ('coupon',)

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user')
		super(CouponUserForm, self).__init__(*args, **kwargs)


class CouponUseForm(forms.ModelForm):

	class Meta:
		model = CouponUser
		fields = ('coupon',)


from django.shortcuts import (
	render, redirect
)
from django.urls import reverse, reverse_lazy
from django.utils import timezone

from django.views.generic import (
	View, CreateView, TemplateView,
)

from .forms import (
	CouponForm, CouponUserForm
)
from .models import Coupon, CouponUser

from django.contrib.auth.models import User

from .utils import CouponSystem

class CouponView(View):

	def get(self, request, *arg, **kwargs):
		return render(request, 'coupon/coupon_home.html', {})


class CouponCreateView(CreateView):
	model = CouponUser
	template_name = 'coupon/coupon_create.html'
	form_class = CouponUserForm
	success_url = reverse_lazy('coupon:coupon_success')

	def get_form_kwargs(self):
		kwargs = super(CouponCreateView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs

	def form_valid(self, form):
		couponuser = form.save(commit=False)
		couponuser.user = self.request.user
		couponuser.save()
		return super().form_valid(form)
		# return HttpResponseRedirect(self.get_success_url())


class CouponDisplayView(View):

	def get(self, request, *args, **kwargs):
		user = self.request.user
		coupon_list = CouponUser.active_objects.filter(user=user)
		context = {
			'coupon_list': coupon_list
		}
		return render(request, 'coupon/coupon_display.html', context)


class CouponUseView(View):

	def get(self, request, *args, **kwargs):
		user = self.request.user
		coupon_list = CouponUser.active_objects.filter(user=user)
		context = {
			'coupon_list': coupon_list
		}
		return render(request, 'coupon/coupon_use.html', context)

	def post(self, request, *args, **kwargs):
		if request.POST.get('coupon') != None:
			coupon_id = request.POST.get('coupon')
			CouponSystem().coupon_use(coupon_id)
		# else 아무것도 선택하지 않았을 때
		else:
			return redirect('coupon:coupon_use')

		request.session['coupon_id'] = coupon_id
		return redirect('coupon:coupon_success')


class CouponReturnView(View):
	
	def get(self, request, *args, **kwargs):
		user = self.request.user
		coupon_list = CouponUser.inactive_objects.filter(user=user)
		context = {
			'coupon_list': coupon_list
		}
		return render(request, 'coupon/coupon_return.html', context)

	def post(self, request, *args, **kwargs):
		if request.POST.get('coupon') != None:
			coupon_id = request.POST.get('coupon')
			CouponSystem().coupon_return(coupon_id)
		else:
			return redirect('coupon:coupon_return')
		return redirect('coupon:coupon_success')		


class SuccessView(View):
	def get(self, request, *args, **kwargs):
		coupon_id = self.request.session['coupon_id']
		coupon = CouponUser.objects.get(pk=coupon_id)
		return render(request, 'coupon/success.html', {'coupon': coupon})


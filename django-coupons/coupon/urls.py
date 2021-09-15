from django.urls import path, include

from . import views

app_name = 'coupon'

urlpatterns = [
	path('', views.CouponView.as_view(), name='coupon_home'),
    path('create/', views.CouponCreateView.as_view(), name='coupon_create'),
    path('display/', views.CouponDisplayView.as_view(), name='coupon_display'),
    path('use/', views.CouponUseView.as_view(), name='coupon_use'),
    path('return/', views.CouponReturnView.as_view(), name='coupon_return'),
    path('success/', views.SuccessView.as_view(), name='coupon_success')
]
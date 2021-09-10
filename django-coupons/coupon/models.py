from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Campaign(models.Model):
	name = models.CharField(
		max_length=255,
		unique=True,
		verbose_name='캠페인',
	)
	description = models.TextField(
		blank=True,
		verbose_name='설명',
	)

	class Meta:
		ordering = ["name"]
		verbose_name = '캠페인'
		verbose_name_plural = '캠페인'

	def __str__(self):
		return self.name


class Coupon(models.Model):

	COUPON_TYPE=(
		('PERCENT','퍼센트'), ('VALUE','값')
	)
	WEEKDAY_CHOICES = (
		(0, '월'), (1, '화'), 
		(2, '수'), (3, '목'), 
		(4, '금'), (5, '토'), (6, '일')
	)


	title = models.CharField(
		verbose_name='이름',
		max_length=50
	)
	description = models.CharField(
		verbose_name='설명',
		max_length=100
	)
	type = models.CharField(
		verbose_name='타입',
		max_length=10,
		choices=COUPON_TYPE,
		default='CASH'
	)
	value = models.DecimalField(
		verbose_name='값',
		default=0.00,
		max_digits=7,
		decimal_places=2,
		validators=[MinValueValidator(0)],
	)
	weekday = models.CharField(
		verbose_name='요일',
		blank=True,
		choices=WEEKDAY_CHOICES,
		validators=[MinValueValidator(0), MaxValueValidator(6)]
	)
	time = models.SmallIntegerField(
		null=True,
		blank=True,
		validators=[MinValueValidator(0), MaxValueValidator(24)],
	)
	days = models.SmallIntegerField(
		default=7
	)
	is_active = models.BooleanField(
		default=True
	)
	created_at = models.DateField(
		verbose_name='생성일',
		auto_now_add=True
	)
	campaign = models.ForeignKey(
		Campaign,
		blank=True,
		null=True,
		on_delete=models.CASCADE,
		related_name="coupons",
	)
	# MANAGEMENT OTHER FIELD
	# other = models.ForeignKey(Other)...

	class Meta:
		ordering = ["created_at"]
		verbose_name = '쿠폰'
		verbose_name_plural = '쿠폰'

	def __str__(self):
		return self.title



class CouponUser(models.Model):
	user = models.ForeignKey(
		User,
		verbose_name='유저'
	)
	coupon = models.ForeignKey(
		Coupon,
		verbose_name='쿠폰'
	)
	created_at = models.DateField(
		verbose_name='생성일',
		default=timezone.now
	)
	expired_at = models.DateField(
		verbose_name='만료일',
		default=timezone.now
	)
	used_at = models.DateTimeField(
		verbose_name='사용일',
		null=True, blank=True
	)

	class Meta:
		verbose_name = '쿠폰유저'
		verbose_name_plural = '쿠폰유저'

	def __str__(self):
		return str(self.user)

@receiver(post_save, sender=CouponUser)
def saved_coupon_user(sender, instance, created, **kwargs):
	if created:
		# 
		days = instance.coupon.days
		expired_at = instance.created_at + timezone.timedelta(days=days)
		instance.expired_at = expired_at
		instance.save()







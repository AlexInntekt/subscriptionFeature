from django.urls import path
from django.views.generic import TemplateView
from . views import MembershipSelectView, PaymentView
app_name = 'memberships'

urlpatterns = [
	path('', MembershipSelectView.as_view(), name='select'),
	path('payment', PaymentView, name='payment'),
	path('test', TemplateView.as_view(template_name='memberships/test.html'), name='test'),

	
]
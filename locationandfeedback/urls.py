from django.urls import path
from locationandfeedback import views


urlpatterns = [
    path('', views.MyFormView.as_view(), name='myformview'),
    path('thankyou/', views.Thankyou.as_view(), name='thankyou'),
]

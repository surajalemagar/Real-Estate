from django.urls import path
from locationandfeedback import views

app_name = 'feedback'
urlpatterns = [
    path('myformview/', views.MyFormView.as_view(), name='myformview'),
    path('post/', views.Post.as_view(), name='post'),
    path('thankyou/', views.Thankyou.as_view(), name='thankyou'),
]

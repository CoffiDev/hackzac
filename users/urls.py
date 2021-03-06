from django.conf.urls import url
from django.views.generic import TemplateView
from .views import YoungSignUp, LogoutView, LoginView

urlpatterns = [
    url(r'^young/login$', TemplateView.as_view(template_name='users/login.html'), name='young_login'),
    url(r'^young/signup$', TemplateView.as_view(template_name='users/signup.html'), name='young_signup'),

    url(r'signUp/young', YoungSignUp.as_view()),

    url(r'logout', LogoutView.as_view()),
    url(r'login', LoginView.as_view())

]

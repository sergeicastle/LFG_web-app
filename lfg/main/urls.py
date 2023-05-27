from django.urls import path

from .views import *

urlpatterns = [
    path('', allideas, name='home'),
    path('createidea', createidea, name='create'),
    path('post/<int:post_id>/', show_post, name='post'),
]

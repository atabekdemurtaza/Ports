from django.urls import path 
from blog.views import blog_category
from blog.views import blog_index
from blog.views import blog_detail

urlpatterns = [
	path("", blog_index, name='blog_index'),
	path('<int:pk>/', blog_detail, name='blog_detail'),
	path("<category>/", blog_category, name='blog_category'),
]
from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("signup/", views.signup, name="signup"), 
	path("signin/", views.signin, name="signin"), 
	path("post/", views.post, name="post"),  
	path("l_comment/<int:p_id>/", views.l_comment, name="l_comment"), 
	path("view_comment/<int:po_id>/", views.view_comment, name="view_comment"), 
	path("delete/<int:post_id>/", views.delete, name="delete"), 
	path("delete_c/<int:com_id>/", views.delete_c, name="delete_c"), 
	path("confirm/<int:p_id>/", views.confirm, name="confirm"), 
	path("create/djform/", views.create_with_djform),
	path("update/<int:post_id>/", views.update, name="update"),
]
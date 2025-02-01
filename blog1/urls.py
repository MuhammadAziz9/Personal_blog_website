from django.urls import path
from .views import postview,postdetail,postcreate,postedit,postdelete

urlpatterns = [
    path('',postview,name='post_view'),
    path('post/<int:id>/',postdetail,name='post_detail'),
    path('post/create/',postcreate,name='post_create'),
    path('post/edit/<int:id>/',postedit,name='post_edit'),
    path('post/delete/<int:id>/',postdelete,name='post_delete')
]
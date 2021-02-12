from posts.views import PostView, CatList, CatDetail
from django.urls import path  

app_name = 'posts'  
urlpatterns = [  
    # path('', PostList.as_view(), name='post-list'),  
    # path('<int:pk>', PostDetail.as_view(), name='post-detail'), 
    path('categories/', CatList.as_view(), name='post-list'),  
    path('categories/<int:pk>', CatDetail.as_view(), name='post-detail'), 
    path('', PostView.as_view(), name='post-list'),  
    path('<int:pk>', PostView.as_view(), name='post-detail'), 
]
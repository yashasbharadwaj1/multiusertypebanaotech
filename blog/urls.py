
from django.urls import path
from .import views

app_name='blog'
urlpatterns=[
   path('', views.index, name='homepage'),
   path('upload/', views.upload, name='upload'),
   path('viewupload/', views.viewupload, name='viewupload'),
   path('viewdraft/', views.viewdraft, name='viewdraft'),
   path('search/',views.post_search,name='post_search'),
   path('<slug:post>/', views.post_single, name='post_single'),
   path('category/<category>/', views.CatListView.as_view(), name='category'),
]  

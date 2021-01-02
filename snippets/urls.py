from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.api_root),
    path('snippets/',views.SnippetListView.as_view(),name = 'snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetailView.as_view(),name = 'snippet-detail'),
    path('users/',views.UserListView.as_view(),name = 'user-list'),
    path('users/<int:pk>',views.UserDetailView.as_view(),name = 'user-detail'),
    path('snippets/<int:pk>/highlight/',views.SnippetHighlightView.as_view(),name = 'snippet-highlight')



]

urlpatterns = format_suffix_patterns(urlpatterns)
from django.urls import path
from core.views import ListarPostsListView

urlpatterns = [
    path('', ListarPostsListView.as_view(), name='home'),
]
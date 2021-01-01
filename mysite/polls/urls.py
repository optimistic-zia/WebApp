from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView

app_name = 'polls'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', PostListView.as_view(), name='home-page'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # the names that we give as a third parameter is used for "href" from templates.
    path('about2/', views.about2, name='about2-page'),
    path('post/new', PostCreateView.as_view(), name='post-create')
]

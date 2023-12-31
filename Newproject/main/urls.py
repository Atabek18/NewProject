from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewDetailView.as_view(), name='new-detail'),
    path('<int:pk>/update', views.NewUpdateView.as_view(), name='new-update'),
    path('<int:pk>/delete', views.NewDeleteView.as_view(), name='new-delete'),
]

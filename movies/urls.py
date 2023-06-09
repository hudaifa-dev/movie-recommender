from django.urls import path

from .views import movie_detail_view, movie_infinte_view, movie_list_view, movie_popular_view

app_name = "movies"
urlpatterns = [
    path("", movie_list_view, name="movie_list"),
    path("<int:pk>/", movie_detail_view, name="movie_detail"),
    path("infinte/", movie_infinte_view, name="movie_infinte"),
    path("popular/", movie_popular_view, name="movie_popular"),
]

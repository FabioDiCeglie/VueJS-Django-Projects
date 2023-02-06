from django.urls import path

from .views import LatestProductsList, ProductDetail, CategoryDetail, search


urlpatterns = [
    path("latest-products/", LatestProductsList.as_view()),
    path("products/search/", search),
    path("products/<slug:category_slug>/<slug:product_slug>/", ProductDetail.as_view()),
    path("products/<slug:category_slug>/", CategoryDetail.as_view()),
    path("products/<slug:category_slug>/", CategoryDetail.as_view())
]

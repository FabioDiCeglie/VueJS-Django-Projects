from django.urls import path

from .views import LatestProductsList, ProductDetail, CategoryDetail


urlpatterns = [
    path("latest-products/", LatestProductsList.as_view()),
    path("products/<slug:category_slug>/<slug:product_slug>/", ProductDetail.as_view()),
    path("products/<slug:category_slug>/", CategoryDetail.as_view())
]

from django.urls import path
from .views import ReviewListCreateView, ReviewDetailView, ProductReviewsView

urlpatterns = [
    path('', ReviewListCreateView.as_view(), name='review-list-create'),
    path('<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('product/<int:product_id>/', ProductReviewsView.as_view(), name='product-reviews'),
]
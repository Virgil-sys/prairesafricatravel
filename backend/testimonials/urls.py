from django.urls import path
from . import views

urlpatterns = [
    path('testimonials/', views.TestimonialListView.as_view(), name='testimonial-list'),
    path('testimonials/create/', views.TestimonialCreateView.as_view(), name='testimonial-create'),
]

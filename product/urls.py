from django.urls import path
from product import views as v
urlpatterns = [
    path('', v.index, name='index'),

    # path('products/', v.ProductsView.as_view(), name='products'),
    # path('product/show/<int:pk>', v.ShowProductView.as_view(), name='show_product'),
    # path('product/add/review/', v.AddReviewView.as_view(), name='add_review'),
    # path('product/search/', v.SearchProductView.as_view(), name='search'),
    # path('login/', v.UserLoginView.as_view(), name='login'),
    # path('register/', v.UserRegisterView.as_view(), name='register'),
    # path('logout/', v.logout_user, name='logout'),


    # path('', v.index, name='index'),
    path('product/about/', v.AboutView.as_view(), name='about'),
    path('product/',v.ProductView.as_view(),name='product'),
    path('testimonial/',v.TestimonialView.as_view(),name='testimonial'),
    path('whyus',v.WhyView.as_view(),name='whyus')
]

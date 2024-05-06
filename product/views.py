from typing import Any
from django.db.models.query import QuerySet
# from django.forms import BaseModelForm
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from product.forms import  ReviewForm, UserCreationForm, RegisterUser, LoginForm
from product.models import Review,  Product
from product.utils import search_product
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.views import generic

# # Create your views here.

# from product.forms import BookForm
from product.models import  Product, Review


# def index(request):
#     return render(request,'pages/index.html')

class IndexView(generic.ListView):
    template_name = 'pages/index.html'
    context_object_name = 'cards'
    
    def get_queryset(self) -> QuerySet[Any]:
        cards = Product.objects.all().order_by('-id')[:3]
        return cards

# # class ShowProductView(generic.DetailView, generic.CreateView):
# #     model = Product
# #     template_name = 'pages/show_product.html'
# #     context_object_name = 'card'
# #     form_class = ReviewForm
    
# #     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
# #         context = super().get_context_data(**kwargs)
# #         context['form_review'] = ReviewForm()
# #         return context
    
class AddReviewView(generic.CreateView):
    template_name = 'pages/products.html'
    form_class = ReviewForm
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        Review.objects.create(text=form.data['text'],assesment=form.data['assesment'], user_id=form.data['user'], product_id = form.data['product'])
 
        return redirect('show_product', form.data['product'])
    
    


# # class ProductsView(generic.ListView):
# #     template_name = 'pages/clothes.html'
# #     context_object_name = 'cards'
    
# #     def get_queryset(self) -> QuerySet[Any]:
# #         cards = Product.objects.all().order_by('-id')
# #         return cards
class SearchProductView(generic.ListView):
    template_name = 'pages/products.html'
    context_object_name = 'card'
    
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Поиск'
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        cards = search_product(self.request)
        return cards
    
# def search(request):
#     template_name = 'pages/clothes.html'
#     cards = search_product(request)
#     context = {
#         'title':"Одежда",
#         'cards':cards        
#     }
#     return render(request, template_name ,context)

class UserRegisterView(generic.CreateView):
    template_name = 'pages/login.html'  
    form_class = RegisterUser
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        return redirect('index')

def logout_user(request):
    logout(request)
    return redirect('index')

class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'pages/login.html'
    
    def get_success_url(self) -> str:
        return reverse_lazy('index')
class AboutView(generic.ListView):
    template_name = 'pages/about.html'
    

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = 'О нас'
        return context
    def get_queryset(self) -> QuerySet[Any]:
        cards = Product.objects.all().order_by('-id')
        return cards
    
class WhyView(generic.ListView):
    template_name = 'pages/why.html'
    context_object_name = 'cards'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = 'Review'
        return context
    

    def get_queryset(self) -> QuerySet[Any]:
        cards = Product.objects.all().order_by('-id')
        return cards
    
    
class TestimonialView(generic.ListView):
    template_name = 'pages/testimonial.html'
    context_object_name = 'cards'


    def get_queryset(self) -> QuerySet[Any]:
        cards = Product.objects.all().order_by('-id')
        return cards

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = 'О нас'
        return context
    
class ProductView(generic.ListView):
    paginate_by = 2
    model = Product
    template_name = 'pages/products.html'
    context_object_name = 'cards'
    
    # form_class = BookForm
    def get_queryset(self) -> QuerySet[Any]:
        cards = Product.objects.all().order_by('-id')
        return cards
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = 'Книги'
        return context
    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     # context['form_review'] = BookForm()
    #     context['title'] = 'Книги'
    #     return context
    

class ShowProduct(generic.DetailView,generic.CreateView):
    model = Product
    template_name = 'pages/show_products.html'
    context_object_name = 'card'
    form_class = ReviewForm
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form_review'] = ReviewForm()
        title = context['card'].title
        context['title'] = f'{title}'
        context['cards'] = self.get_same_card(context['card'].categories.first())
        return context
    
    def get_same_card(self, cat):
        card = Product.objects.filter(categories=cat.id)
        return card
    


class RegisterU(generic.CreateView):
    template_name = 'pages/login.html'
    form_class = RegisterUser

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = 'регистрация'
        return context
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return redirect('index')
    



class Profile(generic.ListView):
    template_name = 'pages/droptown/profile.html'
    context_object_name = 'cards'


    def get_queryset(self) -> QuerySet[Any]:
        cards = Product.objects.all().order_by('-id')
        return cards

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = 'Профиль'
        return context
    

class Order(generic.ListView):
    template_name = 'pages/droptown/corzina.html'
    context_object_name = 'cards'


    def get_queryset(self) -> QuerySet[Any]:
        cards = Product.objects.all().order_by('-id')
        return cards

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = 'Корзина'
        return context
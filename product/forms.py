from django import forms

from product.models import Product
from product.models import choices_review
from product.models import Review
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
class ReviewForm(forms.ModelForm):
    """Review definition."""
    assesment = forms.ChoiceField(choices=choices_review, widget=forms.Select(attrs={'class':'form-select d-inline-flex p-2 bd-highlight', }))
    class Meta:
        model = Review
        fields = ['text', 'assesment']
    
    # TODO: Define form fields here

# class RegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')

# class LoginForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')


# class BookForm(forms.ModelForm):

#     books = forms.BaseForm(data=Book)
#     class Meta:
#         model = Book
#         fields = ['title', 'price', 'categories', 'rating', 'description',]



class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')
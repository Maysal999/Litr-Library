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
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}),label='Имя пользователя')
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'password')

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if username.isupper():
            # raise ValidationError('Имя пользователя должно быть в нижнем регистре!')
            return username
# class BookForm(forms.ModelForm):

#     books = forms.BaseForm(data=Book)
#     class Meta:
#         model = Book
#         fields = ['title', 'price', 'categories', 'rating', 'description',]



class RegisterUser(UserCreationForm):
    email = forms.EmailField(max_length=50,widget=forms.EmailInput(attrs={'class' : 'abc form-control', 'id' : 'exampleFormControlInput1'}),label='Ваша имя')
    username  = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class' : 'abc form-control', 'id' : 'exampleFormControlInput1'}),label='ваша эмайл')
    password1  = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'abc form-control', 'id' : 'inputPassword'}),label='пароль')
    password2  = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'abc form-control', 'id' : 'inputPassword'}),label='подвердения пароля')
  
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
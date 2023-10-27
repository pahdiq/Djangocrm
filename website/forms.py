from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from.models import Product, Categorie

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), required=True)
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}), max_length=30, required=True)
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}), max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1','password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<small>Enter the same password as before, for verification.</small></span>'	


class addfurnitureform(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['catagory', 'image', 'name', 'price', 'size', 'description']


    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        required=False  # Set the field as not required
    )

    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True  # Set the field as required
    )

    price = forms.DecimalField(
        max_digits=7,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=False  # Set the field as not required
    )

    size = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False  # Set the field as not required
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=True  # Set the field as not required
    )
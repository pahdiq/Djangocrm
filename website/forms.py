from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

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



class addfurnitureform(UserCreationForm):
    furniture_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Furniture Name'}), max_length=30, required=True)
    furniture_price = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Furniture Price'}), max_length=30, required=True)
    furniture_description = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Furniture Description'}), max_length=30, required=True)
    furniture_image = forms.ImageField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Furniture Image'}), max_length=30, required=True)
    furniture_category = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Furniture Category'}), max_length=30, required=True)

    class Meta:
        model = User
        fields = ('furniture_name', 'furniture_price', 'furniture_description', 'furniture_image', 'furniture_category')

    def __init__(self, *args, **kwargs):
        super(addfurnitureform, self).__init__(*args, **kwargs)

        self.fields['furniture_name'].widget.attrs['class'] = 'form-control'
        self.fields['furniture_name'].widget.attrs['placeholder'] = 'Furniture Name'
        self.fields['furniture_name'].label = ''
        self.fields['furniture_name'].help_text = '<small>Name your piece of fruniture</small></span>'

        self.fields['furniture_price'].widget.attrs['class'] = 'form-control'
        self.fields['furniture_price'].widget.attrs['placeholder'] = 'Furniture Price'
        self.fields['furniture_price'].label = ''
        self.fields['furniture_price'].help_text = '<small"><li>How musch does your furniture cost?</li></ul>'
        self.fields['furniture_description'].widget.attrs['class'] = 'form-control'
        self.fields['furniture_description'].widget.attrs['placeholder'] = 'Furniture Description'
        self.fields['furniture_description'].label = ''
        self.fields['furniture_description'].help_text = '<small>Enter the detailed description here</small></span>'	

        addfurnitureform.furniture_image = forms.ImageField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Furniture Image'}), max_length=30, required=True)
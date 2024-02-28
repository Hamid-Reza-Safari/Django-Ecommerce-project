from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="ایمیل", widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':''}))
	first_name = forms.CharField(label="نام", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))
	last_name = forms.CharField(label="نام خانوادگی", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['for'] = 'password'
		self.fields['username'].label = 'نام کاربری'
		self.fields['username'].help_text = ''

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = ''
		self.fields['password1'].label = 'رمز عبور'
		self.fields['password1'].help_text = ''

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = ''
		self.fields['password2'].label = 'تایید رمز عبور'
		self.fields['password2'].help_text = ''

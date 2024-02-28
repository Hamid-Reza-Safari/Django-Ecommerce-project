from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _  # Import for translation

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label=_("ایمیل"), widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''}))
    first_name = forms.CharField(label=_("نام"), max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    last_name = forms.CharField(label=_("نام خانوادگی"), max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        error_messages = {
            'username': {
                'unique': (_("نام کاربری تکراری است")),
            },
            'password2': {
                'password_mismatch': (_("رمز عبور تطابق ندارد")),
                'too_similar': (_("رمز عبور بیش از حد شبیه به نام کاربری است")),
                'min_length': (_("رمز عبور باید حداقل 8 کاراکتر داشته باشد")),
                'common': (_("رمز عبور بسیار رایج است")),
            },
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['for'] = 'password'
        self.fields['username'].label = _('نام کاربری')
        self.fields['username'].help_text = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = ''
        self.fields['password1'].label = _('رمز عبور')
        self.fields['password1'].help_text = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = ''
        self.fields['password2'].label = _('تایید رمز عبور')
        self.fields['password2'].help_text = ''

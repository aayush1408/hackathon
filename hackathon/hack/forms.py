from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
# from django.contrib.auth.forms import PasswordChangeForm
from captcha.fields import CaptchaField


GENDER = (
    ('MALE', 'male'),
    ('FEMALE', 'female'),
    ('OTHER', 'other'),
)

STATUS = (
    ('SINGLE', 'single'),
    ('MARRIED', 'married'),
)

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD', widget=forms.TextInput(attrs={'placeholder':'DOB', 'class':'form-control', 'style':'width:200px'}))
    gender = forms.ChoiceField(choices=GENDER, required=True, widget=forms.Select(attrs={'class':'dropdown-item', 'style':'width:200px'}))
    status = forms.ChoiceField(choices=STATUS, required=True, widget=forms.Select(attrs={'class':'dropdown-item', 'style':'width:200px'}))
    # referal_id = forms.CharField(help_text='(make sure you enter it right because this cannot be changed later)',required=False,  widget=forms.TextInput(attrs={'placeholder':'Referal_id', 'class':'form-control', 'style':'width:200px'}))
    pan_number = forms.IntegerField(required=True, max_value=9999999999, widget=forms.NumberInput(attrs={'placeholder':'Pan Number', 'class':'form-control', 'style':'width:200px'}))
    address = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Address', 'class':'form-control', 'style':'width:200px'}))
    city = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'City', 'class':'form-control', 'style':'width:200px'}))
    pincode = forms.IntegerField(required=True, max_value=999999, widget=forms.NumberInput(attrs={'placeholder':'Pincode', 'class':'form-control', 'style':'width:200px'}))
    email = forms.EmailField(help_text='must be unique', required=True, widget=forms.EmailInput(attrs={'placeholder':'E-Mail', 'class':'form-control', 'style':'width:200px'}))
    mobile_number = forms.IntegerField(help_text='must be unique', required=True, max_value=9999999999, widget=forms.NumberInput(attrs={'placeholder':'Mobile Number', 'class':'form-control', 'style':'width:200px'}))
    state = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'State', 'class':'form-control', 'style':'width:200px'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class': 'form-control', 'style':'width:200px'}), label="Password", required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class': 'form-control', 'style':'width:200px'}), label="Confirm Password", required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username','class': 'form-control', 'style':'width:200px'}), label="Username", required=True)
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'First Name', 'class':'form-control', 'style':'width:200px'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Last Name', 'class':'form-control', 'style':'width:200px'}))
    captcha = CaptchaField()
    profile_pic = forms.FileField(required=False)

    def clean_email(self):
        mail = self.cleaned_data['email']
        try:
            match = User.objects.get(email__iexact=mail)
        except:
            return mail
        raise forms.ValidationError("Email already exists.")

    def clean_mobile_number(self):
        m_num = self.cleaned_data['mobile_number']
        try:
            match = Profile.objects.get(mobile_number__iexact = m_num)
        except:
            return m_num
        raise forms.ValidationError('Mobile Number already exist...Try Again!')

    class Meta:
        model = User
        fields = (
                  'username',
                  'first_name',
                  'last_name',
                  'pan_number',
                  'gender',
                  'birth_date',
                  'status',
                  'address',
                  'city',
                  'pincode',
                  'state',
                  'mobile_number',
                  'email',
                  'profile_pic',
                  'password1',
                  'password2',
                  'captcha',
                  )

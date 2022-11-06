from django import forms
from .models import Profile,Account
# from django.contrib.auth.forms 


# class profileforms(forms. ModelForm):
#     phone=forms.CharField()
#     class Meta:
#         model = profile
#         exclude =['user']

class userupdateform(forms.ModelForm):
    # email= forms.EmailField()

    class Meta:
        model = Account
        fields = ['username','email']



class profileUpdateForm(forms.ModelForm):
     class Meta:
        model = Profile
        fields = ['image']
from django import forms
from .models import Account,Profile_update
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
        fields = ['username','first_name','last_name','phone','email']
    


class profileUpdateForm(forms.ModelForm):
     class Meta:
        model = Profile_update
        fields = ['image']
        
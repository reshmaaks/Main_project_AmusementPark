from django import forms
from .models import Account, booking
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




        
        # def clean(self):
        #     cleaned_data=super().clean()
        #     valfirst_name=self.cleaned_data['first_name']
        #     if len(valfirst_name)<2:
        #         raise forms.ValidationError('Name should be more than 2 characters')
        #     valphone=self.cleaned_data['phone']
        #     if len(valphone)==10:
        #         raise forms.ValidationError('Must contain 10 digits')


# class profileUpdateForm(forms.ModelForm):
#      class Meta:
#         model = profile_update
#         fields = ['email']
        



class BookForm(forms.ModelForm):

    class Meta:
        model=booking
        fields=['date','p1_id','p2_id']


        labels={

            'date':'date',
            'p1_id':'Adult',
            'p2_id':'child',
           
        }
widegts={
    'date':forms.DateInput(attrs={'class':'form-control','placeholder':'Date '}),
    'p1_id':forms.Select(attrs={'class':'form-control'}),
    'p2_id':forms.Select(attrs={'class':'form-control'}),

}        
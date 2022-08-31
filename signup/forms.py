from django import forms
import re
 

def validEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return (re.fullmatch(regex, email))

# Minimum 8 characters.
# The alphabet must be between [a-z]
# At least one alphabet should be of Upper Case [A-Z]
# At least 1 number or digit between [0-9]
def validPass(pass1):
    l, u, d = 0, 0, 0
    if (len(pass1) >= 8):
        for i in pass1:
            if (i.islower()):
                l+=1		
            if (i.isupper()):
                u+=1		
            if (i.isdigit()):
                d+=1		

    return (l>=1 and u>=1 and d>=1 and l+u+d==len(pass1))


class SignUpForm(forms.Form):
    fname = forms.CharField(
        max_length=100)
    lname = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class':'input'}))
    email1 = forms.EmailField()
    username = forms.CharField
    pass1 = forms.CharField
    pass2 = forms.CharField

    def clean_email(self):
        data = self.cleaned_data.get('email1')
        if not validEmail(data):
            raise forms.ValidationError('Email is not valid.')

        return data
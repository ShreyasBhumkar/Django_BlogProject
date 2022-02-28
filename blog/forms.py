from django import forms
from blog.models import Add_Blog


class Add_Blog_Form(forms.ModelForm):
    class Meta:
        model = Add_Blog
        exclude = ("User_Name", )
        

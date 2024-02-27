from django import forms

class PostForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
from django import forms
from .models import Blog, Comment

class Blogform(forms.ModelForm):
    class Meta :
        model = Blog
        fields =['topic','text']
        labels ={'topic':'topic','text':'content'}
        widgets={'topic':forms.Textarea(attrs={'rows':1,'cols':80}),'text':forms.Textarea(attrs={'cols':80})}

class Commentform(forms.ModelForm):
    class Meta :
        model = Comment
        fields =['comment']
        labels ={'comment':''}
        widgets ={'comment':forms.Textarea(attrs={'rows':2,'cols':60})}
from django import forms
from .models import Post
 
 
# creating a form
class GeeksForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Post
        fields = ('__all__') # or specify fields individually
        

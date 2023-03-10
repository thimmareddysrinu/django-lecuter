from django import forms
from blogapp.models import Post,Comment



class PostForm(forms.ModelForm):
        class meta():
                   model=Post
                   fields=('author','title','text',)
                   widgets={
                          'title': forms.TextInput(attrs={'class':'textinputclass'}),
                          'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),           
                   }

class CommentForm(forms.ModelForm):
        class meta():
                   model=Comment
                   fields=('text','author',)
                   widgets={
                          'author':forms.TextInput(attrs={'class':'textinputclass'}),
                          'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),            
                     }



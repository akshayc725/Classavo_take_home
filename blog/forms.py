from django import forms
from .models import Post
from mediumeditor.widgets import MediumEditorTextarea

class PostForm(forms.ModelForm):

    def save(self, commit=True):
        post = super(PostForm, self).save(commit=False)
        post.save(commit)
        return post

    class Meta:
        model = Post
        fields = ('text', )
        widgets = {
            'text' : MediumEditorTextarea(),
        }
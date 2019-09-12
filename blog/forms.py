from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'post_text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'myclass'}),
            'post_text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('comment_author', 'comment_text')

        widgets = {
            'comment_author':forms.TextInput(attrs={'class':'myclass'}),
            'comment_text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
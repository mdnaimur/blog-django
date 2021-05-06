from django import forms
from .models import Topic,Post

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'placeholder':'what is on your mind?'}),
     max_length=4000,help_text='The max length of text is 4000.')

    class Meta:
        model =Topic
        fields = ['subject','message']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]
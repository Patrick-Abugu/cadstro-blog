from django import forms
from .import models
class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = [
            'title',
            'body',
            'slug',
            'image',]

#class Feedback(forms.ModelForm):
    #class Meta:
        #model = models.Feedback
class FeedbackForm(forms.Form):
    email = forms.EmailField(required = True, widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}) )
    subject = forms.CharField(max_length=100, required = True, widget=forms.TextInput(attrs={'placeholder': 'Enter subject'}))
    message = forms.CharField(required =True, widget= forms.Textarea(attrs ={'placeholder':'Send us your Feedback'}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name', 'email', 'text']
        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Enter your name'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter your email'}),
            'text':forms.Textarea(attrs={'placeholder':'Enter your comments here'}),
        }


'''class ReplyForm(forms.ModelForm):
    class Meta:
        model = models.Reply
        fields = [
        'name',
        'texts'
        ]
'''

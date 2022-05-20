from django import forms

from comments.models import Comment
from reviews.models import Review


class ReviewForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(ReviewForm,self).__init__(*args,*kwargs)

	content = forms.CharField(widget=forms.Textarea(attrs={'class': 'd-inline w-75 ml-5 form-control '}))
	rate = forms.CharField(widget=forms.NumberInput(attrs={'class': 'control'}))

	class Meta():
		model = Review
		fields = ['content', 'rate']


class CommentForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(CommentForm,self).__init__(*args,*kwargs)

	content = forms.CharField(widget=forms.Textarea(attrs={'class': 'd-block w-75 ml-5 form-control', 'rows':3}))
	
	class Meta():
		model = Comment
		fields = ['content']
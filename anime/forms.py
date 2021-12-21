from django import forms
from .models import Review, Comment, Reply



class ReviewForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(ReviewForm,self).__init__(*args,*kwargs)

	content = forms.CharField(widget=forms.Textarea(attrs={'class': 'control d-block ml-5'}))
	rate = forms.CharField(widget=forms.NumberInput(attrs={'class': 'control'}))

	class Meta():
		model = Review
		fields = ['content', 'rate']


class CommentForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(CommentForm,self).__init__(*args,*kwargs)

	content = forms.CharField(widget=forms.Textarea(attrs={'class': 'control d-block ml-5'}))
	
	class Meta():
		model = Comment
		fields = ['content']
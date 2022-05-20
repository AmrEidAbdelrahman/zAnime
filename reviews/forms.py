from django import forms

from reviews.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rate']

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, *kwargs)

    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'd-inline w-75 ml-5 form-control '}))
    rate = forms.CharField(widget=forms.NumberInput(attrs={'class': 'control'}))



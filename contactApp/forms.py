from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('username','email','title','fdtype','question','image','answer','publishtime','status')
        fdtype_list = (
            ('吐槽交流','吐槽交流'),
            ('功能建议','功能建议'),
            ('Bug反馈','Bug反馈'),
            ('举报投诉','举报投诉'),
        )
        widgets = {
            'fdtype': forms.Select(choices = fdtype_list),
            'image': forms.FileInput(),
        }

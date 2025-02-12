from django import forms

class GroupForm(forms.Form):
    num_japanese = forms.IntegerField(label='日本人の数')
    num_foreign = forms.IntegerField(label='外国人の数')
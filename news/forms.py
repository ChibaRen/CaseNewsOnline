from django import forms

class InputForm(forms.Form):
    name = forms.CharField(
        label='名前',
        max_length=50
        )
    age = forms.IntegerField(
        label='年齢'
        )
    mail = forms.EmailField(
        label='メールアドレス'
        )
    title = forms.CharField(
        label='タイトル',
        max_length=40
        )
    history = forms.CharField(
        label='背景',
        max_length=200,
        widget=forms.Textarea(attrs={'cols':80, 'rows':10})
        )
    done = forms.CharField(
        label='実績',
        max_length=200,
        widget=forms.Textarea(attrs={'cols':80, 'rows':10})
        )
    question = forms.CharField(
        label='問いかけ',
        max_length=200,
        widget=forms.Textarea(attrs={'cols':80, 'rows':10})
        )
    idea = forms.CharField(
        label='考え',
        max_length=100,
        widget=forms.Textarea(attrs={'cols':80, 'rows':10})
        )
    reference = forms.CharField(
        label='参考文献',
        max_length=100,
        widget=forms.Textarea(attrs={'cols':80, 'rows':10})
        )
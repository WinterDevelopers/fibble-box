from django import forms 

from .models import Writer


# Forms
class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer
        exclude = ("user", "date_joined")


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=20)
    text = forms.CharField(widget=forms.Textarea())


class EditPostForm(forms.Form):
    title = forms.CharField(max_length=20)
    text = forms.CharField(widget=forms.Textarea())


class CommentForm(forms.Form):
    username = forms.CharField(max_length=15)
    comment = forms.CharField(
        max_length=100, widget=forms.Textarea(attrs={"placeholder":"Enter your comment"})
    )

    def clean_comment(self):
        comment  = self.cleaned_data["comment"]
        if not comment or comment == " ":
            raise forms.ValidationError('Comment cannot be empty.')
        return comment

    
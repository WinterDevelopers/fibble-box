from django import forms 

from .models import Post, Writer


# Forms
class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer
        exclude = ("user", "date_joined")


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content")



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

    
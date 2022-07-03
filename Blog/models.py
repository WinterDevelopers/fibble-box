from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from pageantry.models import User


# Create your models here.
class Writer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(("First Name"), max_length=50)
    last_name = models.CharField(("Last Name"), max_length=50)
    slug = models.SlugField()
    bio = models.TextField(help_text="About yourself")
    date_joined = models.DateField(("Date Joined"), auto_now_add=True)
    d_o_b = models.DateField(("Date of Birth"), null=True)

    class Meta:
        verbose_name = ("writer")
        verbose_name_plural = ("writers")

    def __str__(self):
        return f"{self.first_name}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}{self.last_name}")
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("Blog:writer_detail", args=[self.first_name, self.last_name])


class Post(models.Model):

    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    text = models.TextField()
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    date_published = models.DateField(("Date Published"), auto_now_add=True)

    class Meta:
        verbose_name = ("post")
        verbose_name_plural = ("posts")

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("Blog:post-detail", kwargs={"slug": self.slug})

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=15)
    comment = models.TextField()
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}, {self.comment[:30]}"


from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200,null=True,blank=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images", default="3.png")
    body = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(null=True,blank=True)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.headline
    
    def save(self, *args, **kwargs):

        if self.slug == None:
            slug = slugify(self.headline)

            has_slug = Post.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.headline) + '-' + str(count)
                has_slug = Post.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)
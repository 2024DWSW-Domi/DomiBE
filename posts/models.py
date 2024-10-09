from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile

class Category(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, related_name='author_profile')
    title = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    body = models.TextField()
    image = models.ImageField(upload_to='post/', default='default.png')
    likes = models.ManyToManyField(User, related_name='like_posts')
    published_date = models.DateTimeField(default=timezone.now)

    def like_count():
        return self.likes.count()
    
class PostCategory(models.Model):
    category = models.ForeignKey(to = Category, on_delete = models.PROTECT, related_name = "categories_postcategory")
    post = models.ForeignKey(to = Post, on_delete = models.CASCADE, related_name = "posts_postcategory")

'''class Like(models.Model):
    post = models.ForeignKey(to = Post, on_delete = models.CASCADE, related_name = "post_likes")
    user = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "user_likes")'''
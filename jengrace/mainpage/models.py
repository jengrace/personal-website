from django.db import models


class UserComment(models.Model):
    timestamp = models.DateTimeField('created', auto_now_add=True)
    name = models.TextField(default="")
    text = models.TextField()

    # this method defines the default behavior of transforming this object to a
    # string, other default methods exist like __dict__ and __len__
    def __str__(self):
        return self.text


class LinkCommentTweet(models.Model):
    timestamp = models.DateTimeField('created', auto_now_add=True)
    name = models.TextField(default="")
    text = models.TextField()
    keyword = models.TextField()

    def __str__(self):
        return self.text

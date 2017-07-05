from django.db import models


class Influencer(models.Model):
    """ influencer 
    """
    username = models.CharField(max_length=200, null=True, blank=True)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    profile_id = models.CharField(max_length=200, null=True, blank=True)
    profile_bio = models.TextField(null=True, blank=True)
    profile_pic = models.CharField(max_length=400, null=True, blank=True)
    profile_posts = models.CharField(max_length=400, null=True, blank=True)
    profile_follows = models.CharField(max_length=200, null=True, blank=True)
    profile_followed_by = models.CharField(max_length=200, null=True, blank=True)

    post_url = models.CharField(max_length=400, null=True, blank=True)
    post_image_url = models.CharField(max_length=200, null=True, blank=True)
    post_category = models.CharField(max_length=200, null=True, blank=True)
    post_comments = models.CharField(max_length=200, null=True, blank=True)
    post_likes = models.CharField(max_length=200, null=True, blank=True)
    post_location = models.CharField(max_length=200, null=True, blank=True)
    post_caption = models.TextField(null=True, blank=True)
    engagement_rate = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.username)



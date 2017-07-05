from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Influencer
from .instagram import InstagramTagMixins


class SearchTagAPI(InstagramTagMixins, viewsets.ViewSet):

    def tag(self, *args, **kwargs):

        data = self.search_by_tag(self.request.data.get('tag'))

        for ig in data:
            user = self.user_profile(ig.get('user').get('id'))
            
            username = user.get('username')
            full_name = user.get('full_name')
            profile_id = user.get('id')
            profile_pic = user.get('profile_picture')
            profile_bio = user.get('bio')
            profile_posts = user.get('counts').get('media')
            profile_follows = user.get('counts').get('follows')
            profile_followed_by = user.get('counts').get('followed_by')

            post_image_url = ig.get('images').get('standard_resolution').get('url')
            post_url = ig.get('link')
            post_category = ig.get('tags')
            post_likes = ig.get('likes').get('count')
            post_comments = ig.get('comments').get('count')
            post_location = ig.get('location')
            post_caption = ig.get('caption').get('text')

            # create influencer
            Influencer.objects.create(
                        username            = username,
                        full_name           = full_name,
                        profile_id          = profile_id,
                        profile_bio         = profile_bio,
                        profile_pic         = profile_pic,
                        profile_posts       = profile_posts,
                        profile_follows     = profile_follows,
                        profile_followed_by = profile_followed_by,
                        post_url            = post_url,
                        post_image_url      = post_image_url,
                        post_category       = post_category,
                        post_comments       = post_comments,
                        post_likes          = post_likes,
                        post_location       = post_location,
                        post_caption        = post_caption
                    )

        return Response({}, status=200)


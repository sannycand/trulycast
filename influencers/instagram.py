from allauth.socialaccount.models import SocialToken
from urllib import request, parse

import json

class InstagramTagMixins(object):

    def __init__(self, *args, **kwargs):
        return super(InstagramTagMixins, self).__init__(*args, **kwargs)

    def _get_access_token(self):
        return SocialToken.objects.first().token

    def search_by_tag(self, tag):
        response = request.urlopen(
            'https://api.instagram.com/v1/tags/{tag}/media/recent?access_token={token}'.format(
                tag=tag,
                token=self._get_access_token(),
            ))
        data = json.loads(response.read().decode('utf-8'))['data']
        return data

    def user_profile(self, user_id):
        response = request.urlopen(
            'https://api.instagram.com/v1/users/{user_id}/?access_token={token}'.format(
                user_id=user_id,
                token=self._get_access_token(),
            ))
        data = json.loads(response.read().decode('utf-8'))['data']
        return data

from transformer.registry import register
from transformer.transforms.base import BaseTransform
import re

class TweetMentionsExtractTransform(BaseTransform):

    category = 'tweet'
    name = 'mentions_extract'
    label = 'Extract Mentions'
    help_text = 'Find all mentions in a tweet.'

    noun = 'Text'
    verb = 'find all mentions in a tweet'

    def transform(self, tweet_input, **kwargs):
        if not tweet_input:
            return []

        return re.findall(r'.?@([a-zA-Z0-9_]+)', tweet_input)

register(TweetMentionsExtractTransform())

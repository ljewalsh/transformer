from transformer.registry import register
from transformer.transforms.base import BaseTransform
import re

class TweetHashtagsExtractTransform(BaseTransform):

    category = 'tweet'
    name = 'hashtags_extract'
    label = 'Extract Hashtags'
    help_text = 'Find all hashtags in a string.'

    noun = 'Text'
    verb = 'find all hashtags in a string'

    def transform(self, tweet_input, **kwargs):
        if not tweet_input:
            return []

        matches = re.findall(r'.?#([a-zA-Z][a-zA-Z0-9]+)', tweet_input)
        return matches

register(TweetHashtagsExtractTransform())

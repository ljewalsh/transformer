from transformer.registry import register
from transformer.transforms.base import BaseTransform
import re

class StringHashtagExtractTransform(BaseTransform):

    category = 'string'
    name = 'hashtag_extract'
    label = 'Extract Hashtag'
    help_text = 'Find all hashtags in a string.'

    noun = 'Text'
    verb = 'find all hashtags in a string'

    def transform(self, str_input, **kwargs):
        if not str_input:
            return u''

        matches = re.findall(r'[A-Z]?[a-z]?#([a-z]+)', str_input)
        return matches

register(StringHashtagExtractTransform())

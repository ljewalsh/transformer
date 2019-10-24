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
            return []

        matches = re.findall(r'.?#([a-zA-Z][a-zA-Z0-9]+)', str_input)
        return matches

register(StringHashtagExtractTransform())

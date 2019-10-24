from transformer.registry import register
from transformer.transforms.base import BaseTransform
import re

class StringMentionExtractTransform(BaseTransform):

    category = 'string'
    name = 'mention_extract'
    label = 'Extract Mention'
    help_text = 'Find all mentions in a string.'

    noun = 'Text'
    verb = 'find all mentions in a string'

    def transform(self, str_input, **kwargs):
        if not str_input:
            return []

        return re.findall(r'.?@([a-zA-Z0-9_]+)', str_input)

register(StringMentionExtractTransform())

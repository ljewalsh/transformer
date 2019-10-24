import unittest
import hashtag_extract

class TestStringHashtagExtractTransform(unittest.TestCase):
    def test_hashtag_extract(self):
        transformer = hashtag_extract.StringHashtagExtractTransform()
        self.assertEqual(transformer.transform(u'[]'), [])
        self.assertEqual(transformer.transform(None), [])
        self.assertEqual(transformer.transform(u'I have no hashtags'), [])
        self.assertEqual(transformer.transform(u'I have a hashtag #hashtag'), [u'hashtag'])
        self.assertEqual(transformer.transform(u'I have two hashtags #hashtag #anotherhashtag'), [u'hashtag', u'anotherhashtag'])
        self.assertEqual(transformer.transform(u'#myhashtag is at the start of my string'), ['myhashtag'])

        # Digits and punctuation should not be captured
        self.assertEqual(transformer.transform(u'#200'), [])
        self.assertEqual(transformer.transform(u'#.'), [])
        self.assertEqual(transformer.transform(u'#,'), [])
        self.assertEqual(transformer.transform(u'#,,'), [])
        self.assertEqual(transformer.transform(u'#,.'), [])
        self.assertEqual(transformer.transform(u'#+'), [])
        self.assertEqual(transformer.transform(u'#-'), [])
        self.assertEqual(transformer.transform(u'#+,'), [])
        self.assertEqual(transformer.transform(u'#+,.'), [])

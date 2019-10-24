import unittest
import hashtags_extract

class TestTweetHashtagsExtractTransform(unittest.TestCase):
    def test_hashtags_extract(self):
        transformer = hashtags_extract.TweetHashtagsExtractTransform()
        self.assertEqual(transformer.transform(u'[]'), [])
        self.assertEqual(transformer.transform(None), [])
        self.assertEqual(transformer.transform(u'I have no hashtags'), [])
        self.assertEqual(transformer.transform(u'I have a hashtag #hashtag'), [u'hashtag'])
        self.assertEqual(transformer.transform(u'My #HASHTAG is capitalised'), [u'HASHTAG'])
        self.assertEqual(transformer.transform(u'My #ha5htag includes a number'), [u'ha5htag'])
        self.assertEqual(transformer.transform(u'I have two hashtags #hashtag #anotherhashtag'), [u'hashtag', u'anotherhashtag'])
        self.assertEqual(transformer.transform(u'#myhashtag is at the start of my string'), ['myhashtag'])

        # Hashtags with digits at the start should not be captured
        self.assertEqual(transformer.transform(u'#2times'), [])

        # Hastags with punctuation should not be captured
        self.assertEqual(transformer.transform(u'#.'), [])
        self.assertEqual(transformer.transform(u'#,'), [])
        self.assertEqual(transformer.transform(u'#,,'), [])
        self.assertEqual(transformer.transform(u'#,.'), [])
        self.assertEqual(transformer.transform(u'#+'), [])
        self.assertEqual(transformer.transform(u'#-'), [])
        self.assertEqual(transformer.transform(u'#+,'), [])
        self.assertEqual(transformer.transform(u'#+,.'), [])

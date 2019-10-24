import unittest
import mentions_extract

class TestTweetMentionExtractTransform(unittest.TestCase):
    def test_mentions_extract(self):
        transformer = mentions_extract.TweetMentionsExtractTransform()
        self.assertEqual(transformer.transform(u'[]'), [])
        self.assertEqual(transformer.transform(None), [])
        self.assertEqual(transformer.transform(u'I have no mentions'), [])
        self.assertEqual(transformer.transform(u'I have a @mention'), [u'mention'])
        self.assertEqual(transformer.transform(u'My mention has @CAPITALISATION'), [u'CAPITALISATION'])
        self.assertEqual(transformer.transform(u'My @ment1on includes a number'), [u'ment1on'])
        self.assertEqual(transformer.transform(u'My @mention_includes an underscore'), [u'mention_includes'])
        self.assertEqual(transformer.transform(u'I have two mentions: @mention, @anothermention'), [u'mention', u'anothermention'])
        self.assertEqual(transformer.transform(u'@mymention is at the start of my string'), ['mymention'])

        # Mentions with punctuation should not be captured
        self.assertEqual(transformer.transform(u'@.'), [])
        self.assertEqual(transformer.transform(u'@,'), [])
        self.assertEqual(transformer.transform(u'@,,'), [])
        self.assertEqual(transformer.transform(u'@,.'), [])
        self.assertEqual(transformer.transform(u'@+'), [])
        self.assertEqual(transformer.transform(u'@-'), [])
        self.assertEqual(transformer.transform(u'@+,'), [])
        self.assertEqual(transformer.transform(u'@+,.'), [])

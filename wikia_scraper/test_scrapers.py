"""
"""

import unittest

#from . import scrapers
import scrapers

class EpisodeSummary(unittest.TestCase):
    """
    """

    def test_scrape_episode_summary(self):
        """
        """
        expected = "Owl's Well That Ends Well is the twenty-fourth episode of the first season of My Little Pony Friendship is Magic. In this episode, Spike grows jealous when Twilight Sparkle befriends an owl and appoints it as a second personal assistant. The title of the episode is a play on the phrase \"all's well that ends well.\""
        actual = scrapers.MetadataScrapers.scrape_episode_summary("https://mlp.fandom.com/wiki/Owl%27s_Well_That_Ends_Well")[0]
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

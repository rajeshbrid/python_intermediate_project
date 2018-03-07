import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))

from unittest import TestCase
from q07_get_unique_teams_set.build import get_unique_teams_set

class TestGet_unique_teams_set(TestCase):
    def test_get_unique_teams_set_return(self):
        teams = get_unique_teams_set()
        actual = {b'Deccan Chargers', b'Kings XI Punjab', b'Chennai Super Kings', b'Mumbai Indians',
                  b'Rajasthan Royals', b'Pune Warriors', b'Kolkata Knight Riders'}
        self.assertEqual(teams, actual, "The Expected teams do not match the actual teams")
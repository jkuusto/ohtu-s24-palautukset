import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_haku_loytaa_oikean_pelaajan(self):
        player = self.stats.search("Kurri")

        self.assertAlmostEqual(str(player), "Kurri EDM 37 + 53 = 90")

    def test_haku_ei_loyda_pelaajaa(self):
        player = self.stats.search("Kurre")

        self.assertAlmostEqual(player, None)

    def test_joukkueen_pelaajat(self):
        players = sorted(self.stats.team("EDM"), key=lambda plr: plr.name)

        self.assertAlmostEqual(len(players), 3)
        self.assertAlmostEqual(str(players[0]), "Gretzky EDM 35 + 89 = 124")
        self.assertAlmostEqual(str(players[1]), "Kurri EDM 37 + 53 = 90")
        self.assertAlmostEqual(str(players[2]), "Semenko EDM 4 + 12 = 16")

    def test_top_pelaajat(self):
        top = self.stats.top(3)

        self.assertAlmostEqual(len(top), 3)
        self.assertAlmostEqual(str(top[0]), "Gretzky EDM 35 + 89 = 124")
        self.assertAlmostEqual(str(top[1]), "Lemieux PIT 45 + 54 = 99")
        self.assertAlmostEqual(str(top[2]), "Yzerman DET 42 + 56 = 98")
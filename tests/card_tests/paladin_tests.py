import random
import unittest
from hsgame.agents.basic_agents import PredictableBot, DoNothingBot
from tests.testing_agents import SpellTestingAgent, MinionPlayingAgent
from tests.testing_utils import generate_game_for

from hsgame.cards import *

__author__ = 'Daniel'

class TestPaladin(unittest.TestCase):

    def setUp(self):
        random.seed(1857)


    def testPaladinPower(self):
        game = generate_game_for(AvengingWrath, MogushanWarden, PredictableBot, DoNothingBot)

        for turn in range(0, 3):
            game.play_single_turn()

        self.assertEqual(1, len(game.current_player.minions))
        self.assertEqual(1, game.current_player.minions[0].attack_power)
        self.assertEqual(1, game.current_player.minions[0].defense)
        self.assertEqual("Silver Hand Recruit", game.current_player.minions[0].card.name)


    def testAvengingWrath(self):
        game = generate_game_for(MogushanWarden, AvengingWrath, MinionPlayingAgent, SpellTestingAgent)

        game.play_single_turn()
        game.play_single_turn()
        game.play_single_turn()
        game.play_single_turn()
        game.play_single_turn()
        game.play_single_turn()
        game.play_single_turn()
        game.play_single_turn()
        game.play_single_turn()
        game.play_single_turn()
        game.play_single_turn()
        game.play_single_turn()

        #The random numbers work so that Avenging Wrath hits the player once, first minion once, second minion four times and third minion two times (total of eight hits)
        self.assertEqual(29, game.other_player.health)
        self.assertEqual(3, len(game.other_player.minions))
        self.assertEqual("Mogu'shan Warden", game.other_player.minions[0].card.name)
        self.assertEqual("Mogu'shan Warden", game.other_player.minions[1].card.name)
        self.assertEqual("Mogu'shan Warden", game.other_player.minions[2].card.name)
        self.assertEqual(6, game.other_player.minions[0].defense)
        self.assertEqual(3, game.other_player.minions[1].defense)
        self.assertEqual(5, game.other_player.minions[2].defense)

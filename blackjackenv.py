#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" BlackJack Environment """

from random import randint
from pybrain.rl.environments.environment import Environment

class BlackjackEnv(Environment):
    """ A (terribly simplified) Blackjack game implementation of an environment. """

    # the number of action values the environment accepts
    indim = 2

    # the number of sensor values the environment produces
    outdim = 21

    hand_value = 0

    def getSensors(self):
        """
        The currently visible state of the world
        The observation may be stochastic - repeated calls returning different values
            :rtype: by default, this is assumed to be a numpy array of doubles
        """
        self.hand_value = randint(self.indim, self.outdim) - 1
        return [float(self.hand_value),]

    def performAction(self, action):
        """
        Perform an action on the world that changes it's internal state (maybe stochastically).
            :key action: an action that should be executed in the Environment.
            :type action: by default, this is assumed to be a numpy array of doubles
        """
        return action

    def reset(self):
        """
        Most environments will implement this optional method that allows for reinitialization.
        """

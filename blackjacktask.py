#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" BlackJack Task """

from random import randint
from pybrain.rl.environments.task import Task

class BlackjackTask(Task):
    """ A task is associating a purpose with an environment. It decides how to evaluate the observations, potentially returning reinforcement rewards or fitness values.
    Furthermore it is a filter for what should be visible to the agent.
    Also, it can potentially act as a filter on how actions are transmitted to the environment. """

    def __init__(self, environment):
        """ All tasks are coupled to an environment. """
        super(BlackjackTask, self).__init__(environment)
        self.action = 0
        self.env = environment
        # we will store the last reward given, remember that "r" in the Q learning formula is the one from the last interaction, not the one given for the current interaction!
        self.lastreward = 0

    def performAction(self, action):
        """ A filtered mapping towards performAction of the underlying environment. """
        self.action = self.env.performAction(action)
        return self.action

    def getObservation(self):
        """ A filtered mapping to getSample of the underlying environment. """
        sensors = self.env.getSensors()
        return sensors

    def getReward(self):
        """ Compute and return the current reward (i.e. corresponding to the last action performed) """
        adv_hand_value = randint(self.indim, self.outdim) - 1
        new_hand_value = self.env.hand_value
        if self.action == 1:
            new_hand_value += randint(2, 21)

        if new_hand_value >= adv_hand_value and new_hand_value <= 21:
            cur_reward = 1.0
        else:
            cur_reward = -1.0

        # print "reward : %s" % cur_reward
        # reward = raw_input("Enter reward: ")

        # retrieve last reward, and save current given reward
        # cur_reward = self.lastreward
        # self.lastreward = reward

        return cur_reward

    @property
    def indim(self):
        return self.env.indim

    @property
    def outdim(self):
        return self.env.outdim

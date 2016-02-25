#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" BlackJack avec du Q-Learning """

from pybrain.rl.learners.valuebased import ActionValueTable
from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners import Q
from pybrain.rl.experiments import Experiment
from pybrain.rl.explorers import EpsilonGreedyExplorer
from blackjacktask import BlackjackTask
from blackjackenv import BlackjackEnv

# define action-value table
# number of states is:
#
#    current value: 1-21
#
# number of actions:
#
#    Stand=0, Hit=1

NB_ITERATION = 300
MIN_VAL = 2
MAX_VAL = 21

def run():
    """ Main function """
    av_table = ActionValueTable(MAX_VAL, MIN_VAL)
    av_table.initialize(0.)

    # define Q-learning agent
    q_learner = Q(0.5, 0.1)
    q_learner._setExplorer(EpsilonGreedyExplorer(0.0))
    agent = LearningAgent(av_table, q_learner)

    # define the environment
    env = BlackjackEnv()

    # define the task
    task = BlackjackTask(env)

    # finally, define experiment
    experiment = Experiment(task, agent)

    # ready to go, start the process
    for i in range(NB_ITERATION):
        experiment.doInteractions(1)
        agent.learn()
        # agent.reset()

    for i in range(MAX_VAL):
        print "The AV Value At ", (i+1), " is: ", av_table.getActionValues(i), av_table.getActionValues(i)[1] - av_table.getActionValues(i)[0]

run()

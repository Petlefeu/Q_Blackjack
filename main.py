#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" BlackJack with Q-Learning """

from pybrain.rl.learners.valuebased import ActionValueTable
from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners import Q
from pybrain.rl.experiments import Experiment
from pybrain.rl.explorers import EpsilonGreedyExplorer
from blackjacktask import BlackjackTask
from blackjackenv import BlackjackEnv

# Debug
# from pdb import set_trace as st
VERBOSE = False

NB_ITERATION = 300
MIN_VAL = 2
MAX_VAL = 21
Q_ALPHA = 0.2
Q_GAMMA = 0.2

def run():
    """
    number of states is:
    current value: 0-20

    number of actions:
    Stand=0, Hit=1 """

    # define action value table
    av_table = ActionValueTable(MAX_VAL, MIN_VAL)
    av_table.initialize(0.)

    # define Q-learning agent
    q_learner = Q(Q_ALPHA, Q_GAMMA)
    q_learner._setExplorer(EpsilonGreedyExplorer(0.0))
    agent = LearningAgent(av_table, q_learner)

    # define the environment
    env = BlackjackEnv()

    # define the task
    task = BlackjackTask(env, verbosity=VERBOSE)

    # finally, define experiment
    experiment = Experiment(task, agent)

    # ready to go, start the process
    for _ in range(NB_ITERATION):
        experiment.doInteractions(1)
        if task.lastreward != 0:
            if VERBOSE:
                print "Agent learn"
            agent.learn()

    print '|First State|Choice 0 (Stand)|Choice 1 (Hit)|Relative value of Standing over Hitting|'
    print '|:-------:|:-------|:-----|:-----|'
    for i in range(MAX_VAL):
        print '| %s | %s | %s | %s |' % (
            (i+1),
            av_table.getActionValues(i)[0],
            av_table.getActionValues(i)[1],
            av_table.getActionValues(i)[0] - av_table.getActionValues(i)[1]
        )

run()

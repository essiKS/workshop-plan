from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

# This document defines very important variables and the shape of your dataset.
# The code (without the comments) is the standard models.py page made by oTree.

# The task of lesson 2 is to make a 3-player public good game.

# You can find a sequence of pages, both in the templates/lesson2 folder and in the pages.py file, already set up.
# These pages explain the game (Introduction), require a decision (Decision), wait for the others to be ready,
# and report the results (Results).


author = 'Your name here'

doc = """
Your app description
"""


# Constants are set once when the session is started. They are common to all participants and may not be changed later.
class Constants(BaseConstants):
    name_in_url = 'lesson2'
    players_per_group = None
    num_rounds = 1

# Task 1: Set up the endowment and multiplication coefficient.
# The endowment is 10 points and the multiplication coefficient is 2.
# You can also add to the number of rounds.
# Notice we need to also adjust the number of participants per group (3).
# If you want, you can update the information on the Instructions.html so that the file directly reads these constants.

# Task 2: Make a comprehension test for the players (under the player model).
# You can ask for example:
# - what is the minimum contribution that a player can make?
# - what is the maximum contribution that a player can make?
# - what is the multiplication coefficient?
# 1. Add the variables under the Player class:
# - f. ex. (indented) maximum_contribution = models.PositiveIntegerField(
#                                   label="What is the maximum contribution that a player can make?")
# - you can fix the answers such that only correct answer will do, using the max and min functions inside the ()
# 2. Add the appropriate form model and form fields under the instructions page in pages.py
# - form_model = 'player'
# - form_fields = ['maximum_contribution]
# 3. Add Django formfields command to the Decision.html


# Task 3: Make the decisions:
# Each participant should make a decision how much to invest of the endowment.
# Note that the 3 decisions are payoff relevant to all participants.
# Furthermore, there are some limits to how much a person can invest. Use min or max to handle this.
# 1. Add the variables under the Group class
# - you can name them for example contribution1, contribution2 and contribution3
# - remember to limit them by the max of the endowment
# - give them a label such as "contribution" or "How much do you wish to contribute?"
# 2. Add the appropriate form model and form fields under the decision page in pages.py
# - because one player should access only one of the contribution form fields, use the following instead of form_fields:
#    def get_form_fields(self):
#        if self.player.id_in_group == 1:
#            return ['contribution1']
#        elif self.player.id_in_group == 2:
#            return ['contribution2']
#        elif self.player.id_in_group == 3:
#            return ['contribution3']
# # Notice the use the id in group, rather than id, to facilitate multiple groups.
# 3. Add Django formfields command to the Decision.html


# Task 4: Payoff function:
# Define a set payoff function under the group model and trigger this after all players have arrived on the wait page
# 1. Add the following function under the group model (notice the indentations)!

#    def set_payoffs(self):
#        for p in self.get_players():
#            if p.id_in_group == 1:
#                p.payoff = Constants.endowment - self.contribution1 + \
#                           2 * (self.contribution1 + self.contribution2 + self.contribution3)
#            elif p.id_in_group == 2:
#                etc.(continue to close all the possible cases....)

# 2. Trigger the function by placing the line under the wait page, after all players arrive function
# (indented) self.group.set_payoffs()


#


# If you need to change some variable for the group, set it under the subsession.
# These variables are shared by all groups and players.
class Subsession(BaseSubsession):
    pass


# Group model is a great place to store any variables that should be accessed by any group member.
class Group(BaseGroup):
    pass


# Individual decisions that concern only the individual are fit to go under the player model.
# Note that there is another similar class called Participant, that is more fundamental to oTree and more hidden.
# We discuss the difference between Player and Participant in the slides.
class Player(BasePlayer):
    pass


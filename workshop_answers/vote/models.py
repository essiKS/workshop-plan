from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from random import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'vote'
    players_per_group = 2
    num_rounds = 2


class Subsession(BaseSubsession):
    color = models.StringField()
    def creating_session(self):
        self.color = self.session.config['treatment']

        if self.round_number == 2:
            original = self.get_group_matrix()
            print("original", original, self.round_number)

            option1324 = [
                [original[0][0], original[1][0]],
                [original[0][1], original[1][1]]
            ]
            option1423 = [
                [original[0][0], original[1][1]],
                [original[0][1], original[1][0]]
            ]

            print("option1324", option1324)
            print("option1423", option1423)

            random_number = random()
            print(random_number)
            if random_number > 0.5:
                self.set_group_matrix(option1324)
            else:
                self.set_group_matrix(option1423)
            print(self.get_group_matrix())





class Group(BaseGroup):
    pass


class Player(BasePlayer):
    vote = models.IntegerField(
        choices=[
            [1, "blue"],
            [0, "red"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    def set_payoffs(self):
        for p in self.get_others_in_group():
            if self.vote ==  p.vote:
                self.payoff = 100
            else:
                self.payoff = 0

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'lesson1'
    players_per_group = 2
    num_rounds = 1
    endowment = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    trust = models.PositiveIntegerField(max=Constants.endowment)
    reciprocity = models.PositiveIntegerField()

    def set_payoffs(self):
        for player in self.get_players():
            if player.role() == 'trustee':
                player.payoff = self.trust * 3 - self.reciprocity
            else:
                player.payoff = Constants.endowment - self.trust + self.reciprocity


class Player(BasePlayer):
    payoff = models.CurrencyField()

    def role(self):
        if self.id_in_group == 1:
            return 'trustor'
        else:
            return 'trustee'


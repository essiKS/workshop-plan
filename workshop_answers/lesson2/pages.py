from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    form_model = 'player'
    form_fields = ['maximum_contribution']


class Decision(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for player in self.group.get_players():
            self.group.total_contributions = self.group.total_contributions + player.contribution

        self.group.set_payoffs()



class Results(Page):
    pass


page_sequence = [
    Instructions,
    Decision,
    ResultsWaitPage,
    Results
]

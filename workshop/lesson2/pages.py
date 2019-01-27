from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    form_model = 'player'
    form_fields = ['maximum_contribution']


class Decision(Page):
    form_model = 'group'
    def get_form_fields(self):
        if self.player.id_in_group == 1:
            return ['contribution1']
        elif self.player.id_in_group == 2:
            return ['contribution2']
        elif self.player.id_in_group == 3:
            return ['contribution3']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass


page_sequence = [
    Instructions,
    Decision,
    ResultsWaitPage,
    Results
]

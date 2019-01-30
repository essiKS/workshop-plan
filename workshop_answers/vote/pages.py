from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['vote']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for player in self.group.get_players():
            player.set_payoffs()


class Results(Page):
    pass


page_sequence = [
    MyPage,
    ResultsWaitPage,
    Results
]

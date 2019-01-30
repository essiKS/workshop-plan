from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Messages


class FirstPage(Page):
    form_model = 'player'
    form_fields = ['name']


class MyPage(Page):
    def vars_for_template(self):
        messages = Messages.objects.filter(group=self.group).values('text')
        print('pages.py', messages)
        return {'messages': messages}


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    FirstPage,
    MyPage,
    ResultsWaitPage,
    Results
]

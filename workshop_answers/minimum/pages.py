from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range

from .models import Constants


class WorkPage(Page):
    timer_text = 'Time left to complete the task:'
    timeout_seconds = 30
    # better to put a large number here while editing, so the page does not time out while you are
    # fixing things.


page_sequence = [
    WorkPage,
]

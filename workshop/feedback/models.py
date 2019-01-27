from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'feedback'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    languages = models.IntegerField(
        label="I recognize the different coding languages (HTML5, JavaScript, Python, Django)"
              " and know when to use which",
        choices=[
            [1, 'Unsure'],
            [2, 'Agree partially'],
            [3, 'Agree']
        ],
        widget=widgets.RadioSelect, )
    dynamic = models.IntegerField(
        label="I can dynamically change the context of a web page",
        choices=[
            [1, 'Unsure'],
            [2, 'Agree partially'],
            [3, 'Agree'],
        ],
        widget=widgets.RadioSelect, )
    syntax = models.IntegerField(
        label="I know the basic syntax of each coding language (HTML5, JavaScript, Python, Django)"
              " and how to search advice online",
        choices=[
            [1, 'Unsure'],
            [2, 'Agree partially'],
            [3, 'Agree'],
        ],
        widget=widgets.RadioSelect, )
    structure = models.IntegerField(
        label="I understand the basic purpose of the main oTree files and how they come together",
        choices=[
            [1, 'Unsure'],
            [2, 'Agree partially'],
            [3, 'Agree'],
        ],
        widget=widgets.RadioSelect, )
    debugging = models.IntegerField(
        label='I can decode error messages (command output and oTree error messages) and find potential solutions',
        choices=[
            [1, 'Unsure'],
            [2, 'Agree partially'],
            [3, 'Agree'],
        ],
        widget=widgets.RadioSelect, )
    inspect = models.IntegerField(
        label='I can inspect the source code on the browser',
        choices=[
            [1, 'Unsure'],
            [2, 'Agree partially'],
            [3, 'Agree'],
        ],
        widget=widgets.RadioSelect, )
    difficulty = models.IntegerField(
        label='I found tasks',
        choices=[
            [1, 'Too easy'],
            [2, 'Ok, varied, both easy and difficult'],
            [3, 'Too difficult (but I understood what was being asked)'],
            [4, 'Buggy, with many mistakes, too long, or unclear']
        ],
        widget=widgets.RadioSelect, )
    stuck = models.StringField(
        label='If you can remember an occasion where you got stuck, please describe here, when it happened.',
        null=True,
        blank=True,
    )
    useful = models.IntegerField(
        label='I found most useful (choose only one)',
        choices=[
            [1, "Learning basic languages: html, Django, JavaScript, Python"],
            [2, "Learning about debugging (console log, code inspection, oTree error feedback)"],
            [3, "Learning about the basic structure of oTree and how to modify it"],
            [4, "Learning about the online resources and how to use them"],
        ],
        widget=widgets.RadioSelect, )
    success = models.LongStringField(
        label='What did you succeed in today?',
        null=True,
        blank=True,
    )
    future = models.LongStringField(
        label='What do you want to learn in the next session?',
        null=True,
        blank=True,
    )
    comment = models.StringField(
        label='You can leave a free comment here:',
        null=True,
        blank=True,
    )
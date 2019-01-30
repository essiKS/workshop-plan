from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from radiogrid import RadioGridField

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
    name = models.StringField(
        label="What is your name?",
    )

ROWS = (
(1, "I like blue"),
(2, "I like red"),
)
COLUMNS = (
(1, "Agreed"),
(2, "Disagreed"),
)

class Player(BasePlayer):
    syntax = models.IntegerField(
        label="I know how to search advice online",
        choices=[
            [1, 'Unsure'],
            [2, 'Agree partially'],
            [3, 'Agree'],
        ],
        widget=widgets.RadioSelect, )
    structure = models.IntegerField(
        label="I feel confident to start coding my oTree projects - I know at least where to start - ",
        choices=[
            [1, 'Unsure'],
            [2, 'Agree partially'],
            [3, 'Agree'],
        ],
        widget=widgets.RadioSelect, )
    debugging = models.IntegerField(
        label='I can decode error messages and find potential out which file is the source of the error',
        choices=[
            [1, 'Unsure'],
            [2, 'Agree partially'],
            [3, 'Agree'],
        ],
        widget=widgets.RadioSelect, )
    breakdown = models.IntegerField(
        label='I can break down a coding project into smaller problems',
        choices=[
            [1, 'Unsure'],
            [2, 'Agree partially'],
            [3, 'Agree'],
        ],
        widget=widgets.RadioSelect, )
    sentences = models.IntegerField(
        label='I can figure out how to do if and for sentences in python, Django, and JavaScript',
        choices=[
            [1, 'Unsure'],
            [2, 'Agree partially'],
            [3, 'Agree'],
        ],
        widget=widgets.RadioSelect, )
    difficulty = models.IntegerField(
        label='I found the course',
        choices=[
            [1, 'Too easy'],
            [2, 'Ok'],
            [3, 'Too difficult'],
        ],
        widget=widgets.RadioSelect, )
    good = models.LongStringField(
        label='Can you remember any good coding practise advice? Please, mention some below:',
        null=True,
        blank=True, )
    useful = models.LongStringField(
        label='I found most useful in the course?',
        null=True,
        blank=True)
    future = models.BooleanField(
        label='I think I will be using oTree in the future',
        choices=[
            [1, 'Yes'],
            [2, 'No'],
        ], )
    missing = models.LongStringField(
        label='I wish the course would have also covered the following:',
        null=True,
        blank=True)
    comment = models.StringField(
        label='You can leave a free comment here:',
        null=True,
        blank=True, )
    name = models.StringField(
        label="What is your name?",
    )
    age = models.PositiveIntegerField(
        label="What is your age?",
        widget=widgets.Slider
    )
    occupation = models.StringField()
    student=models.BooleanField(
        choices=[
            [1, "yes"],
            [2, "no"]
        ],
    )
    department = models.StringField(
        choices=[
            ["Eco", "Economics"],
            ["SPS", "Social and Political Sciences"]
        ],
        widget=widgets.RadioSelect
    )
    expectations = models.CurrencyField(
        label="How many points do you expect to earn?"
    )
    pi = models.FloatField(
        label="How many digits of the mathematical constant Pi do you recall?"
    )
    agree = RadioGridField(rows=ROWS, values=COLUMNS, null=True, require_all_fields=True, verbose_name="Do you agree?")

    def make_field(label):
        return models.IntegerField(
            choices=[
                [1, "agree"],
                [2, "agree somewhat"],
                [3, "don't know"],
                [4, "disagree somewhat"],
                [5, "disagree"]
            ],
            label=label,
            widget=widgets.RadioSelect,
        )

    sunny = make_field("It is sunny outside")










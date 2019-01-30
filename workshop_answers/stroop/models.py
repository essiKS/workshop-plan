from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = ""


class Constants(BaseConstants):
    name_in_url = 'stroop'
    players_per_group = None
    num_rounds = 1
    choices = ['green', 'pink', 'orange', 'blue']


class Subsession(BaseSubsession):
    def creating_session(self):
        # before any page is shown we create initial tasks for each of the players
        for p in self.get_players():
            p.create_stroop()


class Group(BaseGroup):
    ...


class Player(BasePlayer):
    num_tasks_correct = models.IntegerField(initial=0)  # number of tasks correctly solved (initially 0)
    num_tasks_total = models.IntegerField(initial=0)  # total n. of tasks tried (initially 0)
    task_text = models.StringField()
    task_color = models.StringField()
    last_answer = models.StringField()

    def create_stroop(self):
        self.task_text = random.choice(Constants.choices)
        self.task_color = random.choice(Constants.choices)
        self.last_answer = self.task_color
        # if you want to track the text instead, you can change to the text variable instead of the color

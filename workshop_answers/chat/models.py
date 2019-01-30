from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from django.db import models as djmodels

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'chat'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    messages_dump = models.LongStringField()

    def get_channel_group_name(self):
        return 'chat_group_{}'.format(self.pk)


class Player(BasePlayer):
    name = models.StringField()
    last_message = models.StringField()


class Messages(djmodels.Model):
    class Meta:
        ordering = ['-created_at']
    sender = djmodels.ForeignKey(to=Player, related_name='msg')
    group = djmodels.ForeignKey(Group, related_name='receive')
    text = models.StringField()
    created_at = models.DateTimeField(auto_now_add=True)





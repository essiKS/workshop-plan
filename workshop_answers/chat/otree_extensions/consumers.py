from channels.generic.websockets import JsonWebsocketConsumer
# we need to import our Player model to get and put some data there
from chat.models import Player, Group, Messages
import json


class MessageTracker(JsonWebsocketConsumer):
    url_pattern = (r'^/messagetracker/(?P<player_pk>[0-9]+)/(?P<group_pk>[0-9]+)$')

    def clean_kwargs(self):
        self.player_pk = self.kwargs['player_pk']
        self.group_pk = self.kwargs['group_pk']

    def connection_groups(self, **kwargs):
        group_name = self.get_group().get_channel_group_name()
        return [group_name]

    def get_group(self):
        self.clean_kwargs()
        return Group.objects.get(pk=self.group_pk)

    def receive(self, text=None, bytes=None, **kwargs):
        self.clean_kwargs()
        player = Player.objects.get(pk=self.player_pk)
        group = Group.objects.get(pk=self.group_pk)
        if text.get('answer'):
            mes = text['answer']
            print(mes)
            player.last_message = player.name + ': ' + mes
            player.save()
            player.msg.create(text=player.last_message, group=group)
            messages = list(
                Messages.objects.filter(group=group).values())
            group.messages_dump = str(messages)
            group.save()
            active_messages = list(
                Messages.objects.filter(group=group).values('text'))
            active_messages = json.dumps(active_messages)
            self.group_send(group.get_channel_group_name(),{
                             'active_messages': active_messages})
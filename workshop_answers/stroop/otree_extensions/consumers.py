from channels.generic.websockets import JsonWebsocketConsumer
# we need to import our Player model to get and put some data there
from stroop.models import Player


class StroopTracker(JsonWebsocketConsumer):
    # this is the path that should correspond to the one we use in our javascript file
    # the 'player_id' keyword helps us to retrieve the corresponding player data from the database
    url_pattern = (r'^/strooptracker/(?P<player_id>[0-9]+)$')

    # the following 'receive' method is executed automatically by Channels when a message is received from a client
    def receive(self, text=None, bytes=None, **kwargs):
        # using the keyword we get the player
        p = Player.objects.get(id=self.kwargs['player_id'])
        # we receive the answer
        answer = text.get('answer')
        print(answer)
        # if the answer is not empty....
        if answer:
            p.num_tasks_total += 1
            if str(answer) == p.last_answer:
                p.num_tasks_correct += 1
            p.create_stroop()
            p.save()
            self.send({'task_color': p.task_color,
                       'task_text': p.task_text,
                       'num_tasks_correct': p.num_tasks_correct,
                       'num_tasks_total': p.num_tasks_total, })
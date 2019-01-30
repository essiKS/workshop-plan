from channels.routing import route_class
from .consumers import MessageTracker

# the following line builds a path to our consumer
channel_routing = [route_class(MessageTracker, path=MessageTracker.url_pattern), ]

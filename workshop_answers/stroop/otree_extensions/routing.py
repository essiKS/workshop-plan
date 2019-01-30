from channels.routing import route_class
from .consumers import StroopTracker

# the following line builds a path to our consumer
channel_routing = [route_class(StroopTracker, path=StroopTracker.url_pattern), ]
print("stroop routing")
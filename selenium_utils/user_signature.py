import itertools
import logging

logger = logging.getLogger(__name__)


def get_unique_browser_signature_generator(color_depth_list: list, resolution_generator, user_agent_generator):
    """
    Generates a tuple of unique user information.

    Details:
    Iterate through cartesian product of lists/generators. We want to simulate primarily different locations - ips. In
    oeder to do that, we iterate most frequently the ips - the ip_list is the last iterable in the itertools.product.
    """
    for color_depth, resolution, user_agent_raw in itertools.product(
        color_depth_list,
        resolution_generator,
        user_agent_generator
    ):
        screen_width, screen_height = [int(x) for x in resolution]
        user_agent = user_agent_raw[0]

        yield {
            "color_depth": color_depth,
            "screen_width": screen_width,
            "screen_height": screen_height,
            "user_agent": user_agent
        }

from . import user_agents
import random


def get_ua():
    return random.choice(user_agents)

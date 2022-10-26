from urllib.parse import parse_qs
from .helpers import ms


def parse(data) -> dict:

    return dict((ms(k),ms(v[0])) for k,v in  parse_qs(data).items())
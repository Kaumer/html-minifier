from .minify import Minifier, DjangoMinifier
from .version import VERSION, get_version


__version__ = get_version()


__all__ = [
    Minifier.__name__,
    DjangoMinifier.__name__,
    get_version.__name__,
]

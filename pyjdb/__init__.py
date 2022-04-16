try:
    from .day3 import run
except ImportError:
    try:
        from .day2 import run
    except ImportError:
        from .day1 import run

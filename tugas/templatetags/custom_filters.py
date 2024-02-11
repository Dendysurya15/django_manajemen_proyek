# custom_filters.py

from django import template
from datetime import timedelta

register = template.Library()

@register.filter(name='duration_format')
def duration_format(duration):
    if duration is not None and duration != '':
        # Convert to timedelta if the duration is a string
        if isinstance(duration, str):
            try:
                duration = timedelta(days=int(duration))
            except ValueError:
                return None  # Handle invalid duration strings gracefully

        days, seconds = divmod(duration.total_seconds(), 86400)  # 86400 seconds in a day
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
    return None

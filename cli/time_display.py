from datetime import datetime


def get_current_time(self):
    """Get the current time in a formatted string."""
    return datetime.now().strftime("%Hh:%Mm")


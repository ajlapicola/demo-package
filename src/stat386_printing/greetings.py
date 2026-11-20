from rich import print as rich_print
from rich.panel import Panel


def greet(name="everyone", fancy=False):
    message = f"Hello {name}!"
    if fancy:
        rich_print(Panel.fit(message, border_style="cyan"))
    else:
        print(message)


def ungreet(name="everyone", fancy=False):
    message = f"Goodbye {name}!"
    if fancy:
        rich_print(Panel.fit(message, border_style="cyan"))
    else:
        print(message)
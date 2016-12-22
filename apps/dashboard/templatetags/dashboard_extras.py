from django import template

register = template.Library()


def get_page_title(argument):
    switcher = {
        "dashboard": "Dashboard",
        "edition": "Dashboard / Edition",
        2: "two",
    }
    return switcher.get(argument, "No Title")

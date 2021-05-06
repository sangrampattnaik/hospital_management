from django import template
import datetime

register = template.Library()


@register.filter(name='full_date')
def full_date(date):
    return date.strftime("%d %B %Y")

@register.filter(name='month')
def month(value):
    if value == 1:
        return "January".upper()
    elif value == 2:
        return "February".upper()
    elif value == 3:
        return "March".upper()
    elif value == 4:
        return "April".upper()
    elif value == 5:
        return "May".upper()
    elif value == 6:
        return "June".upper()
    elif value == 7:
        return "July".upper()
    elif value == 8:
        return "August".upper()
    if value == 9:
        return "September".upper()
    elif value == 10:
        return "October".upper()
    elif value == 11:
        return "November".upper()
    else:
        return "December".upper()
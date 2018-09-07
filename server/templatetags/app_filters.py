import logging

from django import template
from django import forms

from server.models import Action, Account, Statistics
from server.views import sanitize_js

register = template.Library()


@register.filter(name='isDateable')
def isDateable(field):
    return isinstance(field.field, forms.DateField) or isinstance(field.field, forms.DateTimeField) or isinstance(field.field, forms.TimeField)


@register.filter(name='isDateField')
def isDateField(field):
    return isinstance(field.field, forms.DateField)


@register.filter(name='isDateTimeField')
def isDateTimeField(field):
    return isinstance(field.field, forms.DateTimeField)


@register.filter(name='isTimeField')
def isTimeField(field):
    return isinstance(field.field, forms.TimeField)


@register.filter(name='isAuthenticated')
def isAuthenticated(user):
    return user.is_authenticated


@register.filter(name='sanitizeJS')
def sanitizeJS(string):
    return sanitize_js(string.__str__())


@register.filter(name='getAccountRole')
def getAccountRole(user):
    """
    :param user: The user model
    :return: The string representation of the name for the role
    """
    return Account.to_name(user.account.role).lower()


@register.filter(name='getActivityAction')
def getActivityAction(key):
    """
    :param key: The action number
    :return: The string representation of the name for action
    """
    return Action.to_name(key)

@register.filter(name='getStatisticAction')
def getStatisticAction(key):
    """
    :param key: The statistic number
    :return: The string representation of the name for statistic
    """
    return Statistics.to_statistic(key)
from django import template
register=template.Library()

@register.filter(name="cut")
def cut(value,arg):
    return value.replace(arg, "")

@register.filter(name="addsb")
def add_sb(value):
    return "{} SB".format(value)
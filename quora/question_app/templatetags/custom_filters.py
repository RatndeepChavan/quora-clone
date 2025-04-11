from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    """Custom template filter to get value by key in dictionary type context.

    Args:
        dictionary (dict): context data with dict type
        key (_type_): key for which we want to get value

    Returns:
        str: value of specified key
    """
    return dictionary.get(key)

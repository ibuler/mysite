from django import template


register = template.Library()


@register.filter(name='Lower')
def lower(text):
    return text.lower()


@register.filter
def question_choice_count(question):
    return question.choice_set.count()


@register.filter
def question_choice_count_add(question, num):
    return question.choice_set.count() + int(num)
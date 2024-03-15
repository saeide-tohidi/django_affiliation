from django import template
from persiantools.jdatetime import JalaliDate


register = template.Library()


@register.simple_tag
def date_translate(date, reverse=False):
    jd = JalaliDate(date)
    persian_months = [
        "فروردین",
        "اردیبهشت",
        "خرداد",
        "تیر",
        "مرداد",
        "شهریور",
        "مهر",
        "آبان",
        "آذر",
        "دی",
        "بهمن",
        "اسفند",
    ]
    if reverse:
        tmp = str(jd).split("-")
        return tmp[2] + "-" + tmp[1] + "-" + tmp[0]
    tmp = str(jd).split("-")
    month = persian_months[int(tmp[1]) - 1]
    fa_date = tmp[2] + " " + month + " " + tmp[0]
    return fa_date


@register.simple_tag
def price_translate(price):
    try:
        return "{:,}".format(int(price))
    except Exception as e:
        print(e)
        return "عدم امکان محاسبه قیمت"


@register.simple_tag
def hide_some_char(value):
    if "@" in value:
        value = value.split("@")
        email = value[0][:5]
        final = email + "*****@" + value[1]
    else:
        first = value[:4]
        last = value[-3:]
        final = last + "*****" + first
    return final

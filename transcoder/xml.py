from lxml import etree
from .helpers import ms


def parse(data):
    result = {}

    e = etree.fromstring(data,etree.XMLParser(recover=True,no_network=False))
    for el in e:
        el_tag = ms(el.tag)
        if el.text and el.text.strip():
            value = ms(el.text)
            if not el.tag in result:
                result[el_tag] = value
            else:
                if type(result[el_tag]) == list: 
                    result[el_tag].append(value)
                else:
                    result[el_tag] = [result[el_tag], value]

    return result

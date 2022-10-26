def ms(s):
    if type(s) != str:
        return s.decode('ISO-8859-1')
    return s

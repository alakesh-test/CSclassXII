def celtofar(celcius):
    '''To convert temperature from celcius to fahrenheit'''
    f=9/5*celcius+32
    return f
def fartocel(far):
    '''To convert temperature fahreheit to celcius'''
    cel=(far-32)*5/9
    return cel

print(celtofar(-40))

print(fartocel(-40))



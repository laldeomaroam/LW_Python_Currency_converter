# pylint: disable=missing-docstring
RATES = {'USDEUR':0.85,'GBPEUR':1.13,'CHFEUR':0.86,'EURGBP':0.885,'MURCAD':0.029,'MUREUR':0.022}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    found = 0
    for c_c,r_e in RATES.items():
        if (c_c.startswith(amount[1]) and c_c.endswith(currency)):
            print (round((r_e*float(amount[0]))))
            return round((r_e*float(amount[0])))
            found = found +1

    if found == 0:
        print("None")
#convert(("200","CHF"),"EUR")
#convert(("200","RMB"),"EUR")

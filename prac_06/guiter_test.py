from guitar import Guitar

instrument = Guitar("Gibson L-5 CES", 1922, 16035.40)
instrument_second = Guitar("Another Guitar", 2013, 9999)
print("{} get_age() - Expected {}. Got {}".format(instrument.name, 100,
                                                  instrument.get_age()))
print("{} get_age() - Expected {}. Got {}".format(instrument_second.name, 5,
                                                  instrument_second.get_age()))
print()
print("{} is_vintage() - Expected {}. Got {}".format(instrument.name,
                                                     True,
                                                     instrument.is_vintage()))
print("{} is_vintage() - Expected {}. Got {}".format(instrument_second.name,
                                                     False,
                                                     instrument_second.is_vintage()))
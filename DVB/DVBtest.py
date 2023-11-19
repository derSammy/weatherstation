import dvb

stop = 'Cämmerswalder Straße'
time_offset = 0 # how many minutes in the future, 0 for now
num_results = 10
city = 'Dresden'

abfahrten=dvb.monitor(stop, time_offset, num_results, city)

# Diese Ausgabe ggf. noch mal formatieren, Zeit untereinander und rechtsbündig
# Richtungen aligned

abfahrtstext = f"Abfahrten {stop}:"
for fahrt in abfahrten:
    abfahrtstext += '\n' + f" {fahrt['line']}  {fahrt['direction']}   {fahrt['arrival']}"
print(abfahrtstext)
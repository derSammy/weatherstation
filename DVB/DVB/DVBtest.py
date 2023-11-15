import dvb

stop = 'Dorfhainer Straße'
time_offset = 0 # how many minutes in the future, 0 for now
num_results = 6
city = 'Dresden'

abfahrts_data = dvb.monitor(stop, time_offset, num_results, city)

print(abfahrts_data)
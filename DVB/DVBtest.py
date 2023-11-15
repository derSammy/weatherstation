import dvb

stop = 'Helmholtzstraße'
time_offset = 0 # how many minutes in the future, 0 for now
num_results = 2
city = 'Dresden'

dvb.monitor(stop, time_offset, num_results, city)
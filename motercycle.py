import shelve

with shelve.open('bike') as bike:
    # bike['engine'] = 'petrol'
    bike['colour'] = 'pink'
    # bike['engine_size'] = '10'
    # bike['model'] = '2020'
    del bike['colou']
    for key in bike:
        print(key)


    #print(bike['colou'])
    #print(bike['engine'])


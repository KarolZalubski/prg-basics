car_number = input('Enter car registration number')
is_krakow = car_number[0:2]
if is_krakow == "KK" or is_krakow == "KR":
    print('Car is from Krakow: ', True)
else:
    print('Car is from Krakow:', False)
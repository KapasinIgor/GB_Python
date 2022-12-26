
def find_city(city):
    with open('cities.txt', encoding='utf8') as file:
        lines = file.readlines()
        city = city.lower().title()
        for line in lines:
            if city in line:
                latitude = (line.split('—')[1]).split(',')[0].strip(' ')
                longitude = (line.split('—')[1]).split(',')[1].strip(' \n')
                city = (line.split('—')[0]).strip(' ')
                return latitude, longitude, city
        latitude, longitude, city = None, None, None
        return latitude, longitude, city

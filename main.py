from geopy.geocoders import Nominatim #Подключаем библиотеку
from geopy.distance import geodesic #И дополнения
 
geolocator = Nominatim(user_agent="Tester") #Указываем название приложения
address_1 = str(input('Введите город 1: \n')) #Получаем название первого города
address_2 = str(input('Введите город 2: \n')) #Получаем название второго города
location_1 = geolocator.geocode(address_1) #Получаем полное название первого города
location_2 = geolocator.geocode(address_2) #Получаем полное название второго города
print('Город 1: ', location_1) #Выводим первичные данные
print('Город 2: ', location_2) #Выводим первичные данные
print('Координаты города 1: ', location_1.latitude, location_1.longitude) #Выводим координаты первого города
gps_point_1 = location_1.latitude, location_1.longitude #Выводим координаты первого города
gps_point_2 = location_2.latitude, location_2.longitude #Выводим координаты второго города
print('Координаты города 2: ', location_2.latitude, location_2.longitude) #Выводим общие данные
print('Дистанция между городом', location_1, 'и городом ', location_2, ': ', geodesic(gps_point_1, gps_point_2).kilometers, ' километров') #Выводим полученный результат в километрах
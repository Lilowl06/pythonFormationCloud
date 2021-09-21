t = ()
print(type(t)) # <class 'tuple'> vide

# lat = 45.9632
# lng = 21.7891

coordGPS = (45.9632,21.7891) # chaque élément d'un tuple est un membre
print("Latitude :", coordGPS[0])
# print("Longitude :", coordGPS[2]) # error : tuple index out of range
print("Longitude :", coordGPS[1])

lat, lng = coordGPS #tuple unpacking
print("Latidude :", lat, "Longitude :", lng)

# coordGPS[0] = 66.3344 # error = tuple' object does not support item assignment 
# attention le tuple est une structure en lecture seule, on ne peut pas les réassigner.
data = {"name": "Subhan","Id":33,"Degree":"BSCS"}
for key,value in data.items():
    print(f"These are the keys:{key}, These are the values:{value}")

#nested

traffic_sig = {
    "Kashmir_road":[120,133,110],
    "Railway_road":[70,20,10],
    "Kalma_chowk":[25,15,45],
}
for place,cars_data in traffic_sig.items():

    total = sum(cars_data)
    print(f"From {place} tatal {total} cars passed. ")    





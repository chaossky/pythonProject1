# dictionary in dictionary

travel_log={}
travel_log={"coutry":"Korea","vistited_city":{"Seoul":1,"Pusan":2,"Daegu":3}}

#print(travel_log)

for key in travel_log:
    #print(key)
    for v in travel_log[key]:
        print(travel_log[key][v])
    
#List in dictionary

#Dictionary in list

#List in dictionary
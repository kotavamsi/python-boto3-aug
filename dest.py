a = [{"Name": "Mahesh", "age": 15,"Town": "Hyd"},
     {"Name": "Ramesh", "age": 17,"Town": "Bangalore"},
     {"Name": "somu", "age": 19, "Addr": {"city": "Chennai","street": "Main Street"}},
     {"Name": "sudha", "age": 7, "Town": ["Calcutta","Bangalore","Chennai"]},
     {"Name": "janu", "age": 10, "Town": "Mumbai"}]
# b = a[0]['Name']
# c =a[0]['age']
# d = a[0]['Town']
# print("His name is '{}' , age is '{}' and his town is '{}'".format(b,c,d))
print(a[3]['Town'][2])
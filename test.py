import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name":"me at the zoo2","likes":105152,"views":11231230},{"name":"me at the zoo3","likes":112,"views":1123},
        {"name":"me at the zoo4","likes":10543543,"views":112555120},{"name":"nhji5","likes":10,"views":151515}]

for i in range(len(data)):
    response = requests.put(BASE + "video/"+str(i),data[i])  # put some json data
    print(response.json())

response = requests.get(BASE+"video/2")
print(response.json())
response = requests.patch(BASE+"video/2",{"name":"hello world"})
print(response.json())
response = requests.get(BASE+"video/2")
print(response.json())


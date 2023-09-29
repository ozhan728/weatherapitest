import requests
from datetime import datetime

city = input("Enter City : ")
api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
response = requests.get(api_url, headers={'X-Api-Key': 'sZFDB7p58XXwMQtLUNrasA==EixtyQ5Tr1U9esay'})

newdict = response.json()

# print(newdict)

print("Damaye hava : ",newdict["temp"]," Celsius")


unix_time = newdict["sunset"]
# Convert Unix time to regular time
regular_time = str(datetime.fromtimestamp(unix_time)).split(" ")
unix_time2 = newdict["sunrise"]
regular_time2 = str(datetime.fromtimestamp(unix_time2)).split(" ")
print(f"Tolo aftab : {regular_time2[1]}")
print(f"Ghorob aftab : {regular_time[1]}")
print(f"Tarikh: {regular_time2[0]}")

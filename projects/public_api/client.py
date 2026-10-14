import requests

# === === ==== === === === === ===#
# Getting a response from our API #
# === === ==== === === === === ===#

request = requests.get("https://meksra.pythonanywhere.com/api/calc?a=20&b=4&op=div")
data = request.json()
print(data)

# OUTPUT:
# {"a":20.0,"b":4.0,"operation":"div","result":5.0}



# get the code using postman then convert it into json 
from tkinter import image_names
import requests
poke_name = input("Enter the name of pokemone: ")
url = "https://api.pokemontcg.io/v1/cards?name={}".format(poke_name)
response = requests.get(url)

# print(response)
recieved_data = response.json()
# print(recieved_data)

import matplotlib.pyplot as plt
# url_data = recieved_data["cards"][1]["imageUrl"]
# print(url_data)
url_data = requests.get(recieved_data["cards"][1]["imageUrl"])
with open('./pokemonAPI/poke.png','wb') as f:
    for item in url_data.iter_content(1024):#allways this value is in 2's powers
        f.write(item)

image_data = plt.imread('./poke.png')
plt.imshow(image_data)
plt.show()
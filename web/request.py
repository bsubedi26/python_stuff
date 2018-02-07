import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# raise error if response is bad
res.raise_for_status()

# print(res.text[:100])

file = open('rj.txt', 'w')
file.write(res.text)

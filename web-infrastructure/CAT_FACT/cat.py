import requests 

facts = []
count = 0

for i in range(5):
    response = requests.get("https://catfact.ninja/fact") 
    
    if response.status_code == 200:
        data = response.json()
        facts.append(data["fact"])
        # print(f"Cat fact {i + 1} : {data["fact"]}")
    else: 
        print(f"Failed with status code: {response.status_code}")


for index, fact in enumerate(facts):
    print(f"Cat fact {index + 1}. {fact}")


while catfact < 5:

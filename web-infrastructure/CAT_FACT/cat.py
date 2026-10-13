import requests 

facts = []
catfact = 0

while catfact < 5:
    response = requests.get("https://catfact.ninja/fact") 
    
    if response.status_code == 200:
        data = response.json()
        facts.append(data["fact"])
    else: 
        print(f"Failed with status code: {response.status_code}")

    catfact += 1


for index, fact in enumerate(facts):
    print(f"Cat fact {index + 1}. {fact}")

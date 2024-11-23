import json

file_path: str = "Section18/data.json"

with open(file_path, "r") as file:
    data: dict = json.load(file)
    print(data)

my_json: str = """\
{
    "name": "Mario",
    "age": 33,
    "friends": [
        "Luigi",
        "Toad"
    ],
    "other_info": null
}
"""

data2: dict = json.loads(my_json)
print(data2)

data3: dict = {
    "name": "Mario",
    "age": 33,
    "friends": ["Luigi", "Toad"],
    "other_info": None,
}
file_path2: str = "Section18/data2.json"
with open(file_path2, "w") as file:
    json.dump(data3, file)

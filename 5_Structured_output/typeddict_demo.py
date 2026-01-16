from typing import TypedDict, List

class Person(TypedDict):
    name: str
    age: int
    hobbies: List[str]

new_person: Person = {'name': 'Prashant', 'age': 24}

print(new_person)

def greet(name: str):
    greeting = f'Hello {name[0].capitalize() + name[1:].lower()}!'
    return greeting

print(greet("jane"))

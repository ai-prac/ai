
# Simple Reflex Agent for Vacuum Cleaner World

def vacuum_agent(location, status):

    if status == "Dirty":
        return "Suck"

    elif location == "A":
        return "Move Right"

    elif location == "B":
        return "Move Left"


# Environment
environment = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"

# Agent working
while "Dirty" in environment.values():

    status = environment[location]

    action = vacuum_agent(location, status)

    print("Location:", location)
    print("Status:", status)
    print("Action:", action)

    if action == "Suck":
        environment[location] = "Clean"

    elif action == "Move Right":
        location = "B"

    elif action == "Move Left":
        location = "A"

    print("-------------------")

print("Both rooms are clean!")
print("Final Environment:", environment)

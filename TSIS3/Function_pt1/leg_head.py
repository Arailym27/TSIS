heads=int(input())
legs=int(input())
def count(heads,legs):
    chickens = (legs - (heads * 2)) / 2
    rabbits = heads - chickens
    return chickens, rabbits

chicken,rabbit=count(heads,legs)
print("Number of chickens:",int(chicken))
print("Number of rabbit:",int(rabbit))

# key : value pair
# keys are unique
# values are not
settings = {
    "difficulty": 3,
    "nrLives": 3,
    "startingLevel": 1,
    "canCheat": False,
    "specialPowersAllowed": ["teleportation", "flying", "fireballs"]
}

print settings["nrLives"]

settings["nrLives"] = 50

print settings["nrLives"]


# ITERATE through items and keys
for key in settings:
    print "the option %s is set to %s " % (key, settings[key])

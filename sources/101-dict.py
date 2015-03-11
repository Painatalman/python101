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

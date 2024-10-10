# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

eerste_rivier = rivieren[0].capitalize()
tweede_land_eerste_rivier = rivier_info[rivieren[0]][1].capitalize() 
print(f"De rivier {eerste_rivier} stroomt onder andere door {tweede_land_eerste_rivier}")

tweede_rivier = rivieren[1].capitalize()
eerste_land_tweede_rivier = rivier_info[rivieren[1]][0].capitalize()
print(f"De rivier {tweede_rivier} stroomt onder andere door {eerste_land_tweede_rivier}")


derde_rivier = rivieren[2].capitalize()
derde_land_derde_rivier = rivier_info[rivieren[2]][2].capitalize()
print(f"De rivier {derde_rivier} stroomt onder andere door {derde_land_derde_rivier}")
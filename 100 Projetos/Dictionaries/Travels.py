travel_log= [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_country(country,times,cities):
    travel_log.append({"country": country,"visits": times, "cities": cities})
    cidades=''
    for n in cities:
        if n==cities[len(cities)-1]:
            cidades+=' '+n+'.'
        elif n==cities[0]:
            cidades+=n+','
        else:
            cidades+=' '+n+','
    print(f'Você visitou {country} {times} vezes!')
    print(f'Você esteve em {cidades}')
add_country("Russia",2,["Moscow", "St Petesburg"])
cena_produktu = float(input("Podaj cenę produktu: "))
obnizka_procent = float(input("Podaj procent obniżki: "))
obnizka_kwota = cena_produktu*(obnizka_procent/100)
obnizona_cena = cena_produktu - obnizka_kwota
print(f"Zaoszczędziłeś: {obnizka_kwota}")
print(f"Cena ze zniżką: {obnizona_cena}")


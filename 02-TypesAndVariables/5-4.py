kwota = float(input("Podaj kwotę: "))
vat = 0.23
kwota_vat = kwota * vat
pelna_kwota = kwota + kwota_vat
print(f"Vat = {kwota_vat}")
print(f"Pełna kwota = {pelna_kwota}")


#problemy - 1) ukladani vstupu z bodu jedna do seznamu ukoly;  3) vypsaní seznamu úkolů; 4) smazání ze seznamu úkolŮ


while True:
    print("\n Správce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")

    vyber = float(input("Vyberte možnost (1-4): "))

    
    ukoly = []
    if vyber == 1:
        while True:
            nazev_ukolu = input("Zadejte název úkolu: ").strip()
            popis_ukolu = input("Zadejte popis úkolu: ").strip()
            ukol_id = len(ukoly) + 1
            ukoly.append((ukol_id, nazev_ukolu, popis_ukolu))
            if nazev_ukolu and popis_ukolu:
                break
            print("Všechna pole jsou povinná. Prosím, zkuste to znovu.")
        print(f"Úkol {nazev_ukolu} byl přidán.")

    elif vyber == 2:
            print(ukoly)
        
    elif vyber == 3:
        print(ukoly)
        ukol_id = input("Zadejte číslo úkolu, který chcete odstranit: ")
        ukoly.remove(ukol_id)
        print(f"{ukol_id} byl odstraněn.")

    elif vyber == 4:
        print("Konec programu.")
        break
    
    else:
        print("Neplatná volba. Vybírejte jenom z možností 1-4.")



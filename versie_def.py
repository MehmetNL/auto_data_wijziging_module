def versie_info():
    versie = "v1.8.3"
    ########################### hierboven definitie ########
    print(100 * "-")
    print(30 * " ", f"Auto voorraadbeheer versie {versie}")
    print(100 * "-")

# versie 1.6 auto gegevens verwijderen toegevoegd
# versie 1.7 resultaat aantallen in getallen, en vervolgens lijst geven met de ingevoerde resultaat.
# versie 1.8.1 Bij auto toevoegen worden gegevens nu vannuit rdw opgehaald, alleen kenteken invullen is voldoende,
# indien ontbrekende gegevens worden opgehaald dient gebruiker zelf in te vullen.
# versie 1.8.2 Oudere voertuigen, zijn geen cataloog prijs bekend bij rdw, database verwacht daar wel een waarde ipv None
# if toegepast, indien RDW API None waarde terug keert, wordt de cat. waarde 0 gezet.
# versie 1.8.3 NN in databse opgevangen met user input
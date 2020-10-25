from Manager import Angajat, Manager
from Gestionar import Gestionar
from Operator import Operator
import json

# ID Manager 117712256313
a=True
while True:
    logare = input("Introduceti ID-ul dumeavoastra:\n>")
    read_json_file = open("Lista_angajati.json", "r")
    convert_json_to_dict = json.load(read_json_file)
    read_json_file.close()
    list_ID = []
    for angajat in convert_json_to_dict:
        list_ID.append(convert_json_to_dict[angajat]["ID"])
    if logare not in list_ID:
        print("ID invalid")
        continue
    if str(logare[:2]) == "11":
        while a:
            optiune=int(input("Selectati o optiune:\n1. Adaugare angajat\n2. Eliminare angajat\n3. Modificare calificari angajat\n4. Afisare productie si stoc produse finite\n5. Revenire la introducere ID\n>"))
            try:
                if optiune == 1:
                    functie_angajat=int(input("Doriti sa adaugati1:\n1. Operator nou\n2. Gestionar nou\n0. Revenire la meniul anterior\n>"))
                    if functie_angajat==1:
                        optiune_calificare=int(input("Selectati:\n1. Frigotehnist\n2. Electronist\n3. Instalator\n>"))
                        if optiune_calificare==1:
                            Angajat_nou = Operator(input("Introduceti numele angajatului\n>"),input("Introduceti prenumele angajatului\n>"),int(input("Introduceti anul nasterii\n>")),int(input("Introduceti luna nasterii\n>")),int(input("Introduceti ziua nasterii\n>")), "Frigotehnist")
                        elif optiune_calificare ==2:
                            Angajat_nou=Operator(input("Introduceti numele angajatului\n>"),input("Introduceti prenumele angajatului\n>"),int(input("Introduceti anul nasterii\n>")),int(input("Introduceti luna nasterii\n>")),int(input("Introduceti ziua nasterii\n>")),"Electronist")
                        elif optiune_calificare ==3:
                            Angajat_nou = Operator(input("Introduceti numele angajatului\n>"),input("Introduceti prenumele angajatului\n>"),int(input("Introduceti anul nasterii\n>")),int(input("Introduceti luna nasterii\n>")),int(input("Introduceti ziua nasterii\n>")), "Instalator")
                        Manager.adaugare_angajati(Angajat_nou)
                    elif functie_angajat==2:
                        Angajat_nou=Gestionar(input("Introduceti numele angajatului\n>"),input("Introduceti prenumele angajatului\n>"),int(input("Introduceti anul nasterii\n>")),int(input("Introduceti luna nasterii\n>")),int(input("Introduceti ziua nasterii\n>")))
                        Manager.adaugare_angajati(Angajat_nou)
            except: print("Introduceti o optiune valida!")
            if optiune == 2:
                Manager.eliminare_angajati()
            elif optiune == 3:
                Manager.modificare_calificari()
            elif optiune == 5:
                break
            elif optiune ==4:
                Manager.afisare_productie()
            else:
                continue
    if str(logare[:2]) == "33":
        while True:
            try:
                optiune = int(input("Selectati o optiune:\n1. Productie frigider\n2. Productie cuptor cu microunde\n3. Productie aragaz\n4. Afisare productie si stoc produse finite\n5. Revenire la introducere ID\n>"))
                if optiune == 1:
                    Operator.productie_frigider(logare)
                elif optiune == 2:
                    Operator.productie_cuptor_cu_microunde(logare)
                elif optiune == 3:
                    Operator.productie_aragaz(logare)
                elif optiune==4:
                    Operator.afisare_productie()
                else:
                    break
            except: print("Selectati o optiune valida.")
    if str(logare[:2]) == "55":
        while a:
            try:
                optiune = int(input("Selectati o optiune:\n1. Adaugare materie prima\n2. Utilizare materie prima\n3. Afisare produse finite\n4. Transfer catre puncte de vanzare\n5. Revenire la introducere ID\n>"))
                if optiune == 1:
                    Gestionar.receptie_materie_prima()
                elif optiune == 2:
                    Gestionar.utilizare_materie_prima()
                elif optiune == 3:
                    Gestionar.afisare_productie()
                elif optiune == 4:
                    Gestionar.scoatere_din_gestiune()
                else:
                    break
            except:
                print("Selectati o optiune valida")

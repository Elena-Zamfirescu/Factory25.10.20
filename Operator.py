from Manager import Angajat
import json
class Operator(Angajat):
    def __init__(self,nume,prenume,anul_nasterii,luna_nasterii,ziua_nasterii,calificare):
        super().__init__(nume,prenume,anul_nasterii,luna_nasterii,ziua_nasterii)
        self.calificare=calificare
    def productie_frigider(ID):

        read_json_file = open("Lista_angajati.json", "r")
        convert_json_to_dict = json.load(read_json_file)
        read_json_file.close()

        for angajat in convert_json_to_dict:
            if convert_json_to_dict[angajat]["ID"] == ID:
                calificare = convert_json_to_dict[angajat]["functie/calificare"].lower()
        while True:
            if calificare =="frigotehnist":
                print("Aveti nevoie de:\n1. Tabla - 5 um\n2. Freon - 8 um\npentru fiecare produs\n")
                read_json_file = open("Materie.json", "r")
                convert_json_to_dict = json.load(read_json_file)
                max_FG=round(min(convert_json_to_dict['Tabla']/5,convert_json_to_dict['Freon']/8))
                print(f"Aveti gestiune: Tabla: {convert_json_to_dict['Tabla']} um si Freon: {convert_json_to_dict['Freon']} um, puteti produce maximum {max_FG} produse.")
                numar_FG = int(input("0. Revenire la meniul anterior\nCate frigidere doriti sa produceti?\n>"))
                if numar_FG==0:
                    break
                convert_json_to_dict["Tabla"]-=5*numar_FG
                convert_json_to_dict["Freon"]-=8*numar_FG
                read_json_file.close()

                if convert_json_to_dict["Tabla"]>=0 and convert_json_to_dict["Freon"]>=0:
                    print("Productie finalizata cu succes.\n")
                    new_material = json.dumps(convert_json_to_dict, indent=4)
                    rewrite_json = open("Materie.json", "w")
                    rewrite_json.write(new_material)
                    rewrite_json.close()
                    read_json_file = open("Productie.json", "r")
                    converted_product = json.load(read_json_file)
                    read_json_file.close()
                    converted_product['productie_totala']["Frigidere"] += numar_FG
                    new_production = json.dumps(converted_product, indent=4)
                    rewrite_json = open("Productie.json", "w")
                    rewrite_json.write(new_production)
                    rewrite_json.close()
                    break
                else:
                    print("Nu aveti suficienta materie prima la dispozitie.")
            else:
                print("Nu aveti calificarea necesara pentru a produce frigidere.\nSolicitati schimbarea calificarii sau productia cu un alt operator.\n")
                break


    def productie_aragaz(ID):
        read_json_file = open("Lista_angajati.json", "r")
        convert_json_to_dict = json.load(read_json_file)
        read_json_file.close()

        for angajat in convert_json_to_dict:
            if convert_json_to_dict[angajat]["ID"] == ID:
                calificare = convert_json_to_dict[angajat]["functie/calificare"].lower()
        while True:
            if calificare == "instalator":
                print("Aveti nevoie de:\n1. Tabla - 11 um\n2. Rezistori - 21 um\npentru fiecare produs\n")
                read_json_file = open("Materie.json", "r")
                convert_json_to_dict = json.load(read_json_file)
                max_FG = round(min(convert_json_to_dict['Tabla'] / 11, convert_json_to_dict['Rezistori'] / 21))
                print(
                    f"Aveti gestiune: Tabla: {convert_json_to_dict['Tabla']} um si Rezistori: {convert_json_to_dict['Rezistori']} um, puteti produce maximum {max_FG} produse.")
                numar_FG = int(input("0. Revenire la meniul anterior\nCate aragazuri doriti sa produceti?\n>"))
                if numar_FG == 0:
                    break
                convert_json_to_dict["Tabla"] -= 11 * numar_FG
                convert_json_to_dict["Rezistori"] -= 21 * numar_FG
                read_json_file.close()

                if convert_json_to_dict["Tabla"] >= 0 and convert_json_to_dict["Rezistori"] >= 0:
                    print("Productie finalizata cu succes.\n")
                    new_material = json.dumps(convert_json_to_dict, indent=4)
                    rewrite_json = open("Materie.json", "w")
                    rewrite_json.write(new_material)
                    rewrite_json.close()
                    read_json_file = open("Productie.json", "r")
                    converted_product = json.load(read_json_file)
                    read_json_file.close()
                    converted_product['productie_totala']["Aragazuri"] += numar_FG
                    new_production = json.dumps(converted_product, indent=4)
                    rewrite_json = open("Productie.json", "w")
                    rewrite_json.write(new_production)
                    rewrite_json.close()
                    break
                else:
                    print("Nu aveti suficienta materie prima la dispozitie.")

            else:
                print(
                    "Nu aveti calificarea necesara pentru a produce aragazuri.\nSolicitati schimbarea calificarii sau productia cu un alt operator.\n")
                break


    def productie_cuptor_cu_microunde(ID):
        read_json_file = open("Lista_angajati.json", "r")
        convert_json_to_dict = json.load(read_json_file)
        read_json_file.close()

        for angajat in convert_json_to_dict:
            if convert_json_to_dict[angajat]["ID"] == ID:
                calificare = convert_json_to_dict[angajat]["functie/calificare"].lower()
        while True:
            if calificare == "electronist":
                print("Aveti nevoie de:\n1. Tabla - 2 um\n2. Inductori - 7 um\n3. Capacitori - 12\npentru fiecare produs\n")
                read_json_file = open("Materie.json", "r")
                convert_json_to_dict = json.load(read_json_file)
                max_FG = round(min(convert_json_to_dict['Tabla'] / 2, convert_json_to_dict['Inductori'] / 7,convert_json_to_dict['Capacitori'] / 12))
                print(
                    f"Aveti gestiune: Tabla: {convert_json_to_dict['Tabla']} um, Inductori: {convert_json_to_dict['Inductori']} um si Capacitori: {convert_json_to_dict['Capacitori']} um puteti produce maximum {max_FG} produse.")
                numar_FG = int(input("0. Revenire la meniul anterior\nCate cuptoare cu microunde doriti sa produceti?\n>"))
                if numar_FG == 0:
                    break
                convert_json_to_dict["Tabla"] -= 2 * numar_FG
                convert_json_to_dict["Inductori"] -= 7 * numar_FG
                convert_json_to_dict["Capacitori"] -= 12 * numar_FG
                read_json_file.close()

                if convert_json_to_dict["Tabla"] >= 0 and convert_json_to_dict["Inductori"] >= 0 and convert_json_to_dict["Capacitori"] >= 0:
                    print("Productie finalizata cu succes.\n")
                    new_material = json.dumps(convert_json_to_dict, indent=4)
                    rewrite_json = open("Materie.json", "w")
                    rewrite_json.write(new_material)
                    rewrite_json.close()
                    read_json_file = open("Productie.json", "r")
                    converted_product = json.load(read_json_file)
                    read_json_file.close()
                    converted_product['productie_totala']["Cuptoare cu microunde"] += numar_FG
                    new_production = json.dumps(converted_product, indent=4)
                    rewrite_json = open("Productie.json", "w")
                    rewrite_json.write(new_production)
                    rewrite_json.close()
                    break
                else:
                    print("Nu aveti suficienta materie prima la dispozitie.")

            else:
                print("Nu aveti calificarea necesara pentru a produce cuptoare cu microunde.\nSolicitati schimbarea calificarii sau productia cu un alt operator.\n")
                break


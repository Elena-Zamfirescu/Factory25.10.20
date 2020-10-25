from Manager import Angajat
import json

class Gestionar(Angajat):

    def __init__(self,nume,prenume,anul_nasterii,luna_nasterii,ziua_nasterii,calificare="Gestionar"):
        super().__init__(nume,prenume,anul_nasterii,luna_nasterii,ziua_nasterii)
        self.calificare=calificare
    @staticmethod
    def receptie_materie_prima():
        read_json_file = open("Materie.json", "r")
        convert_json_to_dict = json.load(read_json_file)
        j=1
        while j< len(convert_json_to_dict):
            for i in convert_json_to_dict:
                print(f"{j}. {i}")
                j+=1
        print("0. Revenire la meniul anterior")
        while True:
            mat=int(input("Introduceti cifra corespunzatoare materiei prime.\n>"))
            if mat==1:
                mat="Tabla"
            elif mat ==2:
                mat="Freon"
            elif mat ==3:
                mat = "Rezistori"
            elif mat == 4:
                mat = "Inductori"
            elif mat ==5:
                mat = "Capacitori"
            else:
                break
            cant=int(input("Ce cantitate doriti sa introduceti?\n>"))
            convert_json_to_dict[mat]=convert_json_to_dict[mat]+cant
            new_material = json.dumps(convert_json_to_dict, indent=4)
            rewrite_json = open("Materie.json", "w")
            rewrite_json.write(new_material)
            rewrite_json.close()
            print("Materia prima a fost adaugata")
            break

    @staticmethod
    def utilizare_materie_prima():
        read_json_file = open("Materie.json", "r")
        convert_json_to_dict = json.load(read_json_file)
        j = 1
        while j < len(convert_json_to_dict):
            for i in convert_json_to_dict:
                print(f"{j}. {i}")
                j += 1
        print("0. Revenire la meniul anterior")
        mat = int(input("Introduceti numarul corespunzator materiei prime.\n>"))
        while True:

            if mat==1:
                mat="Tabla"
            elif mat ==2:
                mat="Freon"
            elif mat ==3:
                mat = "Rezistori"
            elif mat == 4:
                mat = "Inductori"
            elif mat ==5:
                mat = "Capacitori"
            else:
                break
            print(f"Cantitatea disponibila este de {convert_json_to_dict[mat]}.")
            cant=int(input("Ce cantitate doriti sa scoateti din gestiune?\n>"))
            convert_json_to_dict[mat]=convert_json_to_dict[mat]-cant
            new_material = json.dumps(convert_json_to_dict, indent=4)
            rewrite_json = open("Materie.json", "w")
            rewrite_json.write(new_material)
            rewrite_json.close()
            print("Materia prima a fost scoasa din gestiune")
    @staticmethod
    def scoatere_din_gestiune():
        a = True
        while a:
            optiune=int(input("Selectati tipul produsului:\n1. Frigid\n2. Aragaz\n3. Cuptor cu microunde\n0. Revenire la meniul anterior\n>"))
            if optiune!=1 and optiune!=2 and optiune!=3:
                a=False
                continue

            read_json_file = open("Productie.json", "r")
            converted_product = json.load(read_json_file)
            read_json_file.close()
            if optiune==1:
                print(f"Aveti pe stoc {converted_product['stoc']['Frigidere']} frigidere.")
                cant = int(input("Cate produse transferati catre punctul de vanzare?\n>"))
                converted_product['stoc']['Frigidere'] -= cant
            elif optiune ==2:
                print(f"Aveti pe stoc {converted_product['stoc']['Aragazuri']} aragazuri.")
                cant = int(input("Cate produse transferati catre punctul de vanzare?\n>"))
                converted_product['stoc']['Aragazuri'] -=cant
            else:
                print(f"Aveti pe stoc {converted_product['stoc']['Cuptoare cu microunde']} cuptoare cu microunde.")
                cant = int(input("Cate produse transferati catre punctul de vanzare?\n>"))
                converted_product['stoc']['Cuptoare cu microunde'] -= cant

            if converted_product['stoc']['Frigidere']>=0 and converted_product['stoc']['Aragazuri']>=0 and converted_product['stoc']['Cuptoare cu microunde']>=0:
                new_production = json.dumps(converted_product, indent=4)
                rewrite_json = open("Productie.json", "w")
                rewrite_json.write(new_production)
                rewrite_json.close()
                print("Produsele au fost eliminate din stoc, va rugam pregatiti expediere!")
            else:
                print("Nu aveti suficiente produse pe stoc, va rugam consultati productia!")
                break

import random
import json
from time import time, ctime

class Fabrica:

    nume_Fabrica="Absintus"
    an_baza_de_date=2020
    def __init__(self, adresa_fabrica, domeniu):
        self.adresa_fabrica=adresa_fabrica
        self.domeniu=domeniu


Fabrica_de_lucru=Fabrica ("Timisoara, str. Lugojului, nr. 18","Productie electro-casnice")


class Angajat:

    def __init__(self,nume,prenume,anul_nasterii,luna_nasterii,ziua_nasterii):
        self.nume=nume
        self.prenume=prenume
        self.anul_nasterii=anul_nasterii
        self.luna_nasterii = luna_nasterii
        self.ziua_nasterii = ziua_nasterii
        self.email=f"{nume}.{prenume}@{Fabrica.nume_Fabrica}.ro"
        # self.calificare=calificare
# creare ID dupa modelul CNP-ului, primele 2 cifre corespund departamentului, urmatoarele 6 se creaza dupa data nasterii,
#iar ultimele 4 sunt random
        id=random.randint(1000, 9999)
        if self.anul_nasterii<2000:
            self.anul_nasterii1 = self.anul_nasterii-1900
        else:
            self.anul_nasterii1 = f"0{self.anul_nasterii - 2000}"

        if int(self.luna_nasterii)< 10:
            self.luna_nasterii = f"0{self.luna_nasterii}"
        else:
            self.luna_nasterii=f"{self.luna_nasterii}"

        if int(self.ziua_nasterii) < 10:
            self.ziua_nasterii = f"0{self.ziua_nasterii}"
        else:
            self.ziua_nasterii=f"{self.ziua_nasterii}"

        if self.__class__.__name__=="Operator":
            id_dep=33
        elif self.__class__.__name__=="Manager":
            id_dep=11
        else:
            id_dep=55
        self.ID = f"{id_dep}{self.anul_nasterii1}{self.luna_nasterii}{self.ziua_nasterii}{id}"
        read_json_file = open("Lista_angajati.json", "r")
        convert_json_to_dict = json.load(read_json_file)
        read_json_file.close()
    # verificare duplicate ID
        list_IDs=[]
        while True:
            for angajat in convert_json_to_dict:
                list_IDs=convert_json_to_dict[angajat]["ID"]
            if self.ID in list_IDs:
                self.ID = f"{id_dep}{self.anul_nasterii1}{self.luna_nasterii}{self.ziua_nasterii}{id}"
            else:
                break

    def afisare_productie():
        while True:
            optiune=int(input("Selectati\n1. Frigidere\n2. Aragazuri\n3. Cuptoare cu microunde\n4. Toate produsele\n0. Revenire la meniul anterior\n"))
            read_json_file = open("Productie.json", "r")
            converted_product = json.load(read_json_file)
            read_json_file.close()
            t1=time()
            if optiune==1:
                print(f"Pana la {ctime(t1)} s-au produs {converted_product['productie_totala']['Frigidere']} frigidere, pe stoc: {converted_product['stoc']['Frigidere']}.\n")
            elif optiune==2:
                print(f"Pana la {ctime(t1)} s-au produs {converted_product['productie_totala']['Aragazuri']} aragazuri, pe stoc {converted_product['stoc']['Aragazuri']}.\n")
            elif optiune==3:
                print(f"Pana la {ctime(t1)} s-au produs {converted_product['productie_totala']['Cuptoare cu microunde']} cuptoare cu microunde, pe stoc {converted_product['stoc']['Cuptoare cu microunde']}.\n")
            elif optiune==4:
                print(f"Pana la {ctime(t1)} s-au produs:\n{converted_product['productie_totala']['Frigidere']} frigidere, pe stoc {converted_product['stoc']['Frigidere']}\n{converted_product['productie_totala']['Aragazuri']} aragazuri, pe stoc {converted_product['stoc']['Aragazuri']}\n{converted_product['productie_totala']['Cuptoare cu microunde']} cuptoare cu microunde, pe stoc {converted_product['stoc']['Cuptoare cu microunde']}.\n")
                break
            elif optiune==0:
                break
            else:
                print("Selectati o optiune valida.")
                continue
class Manager(Angajat):

    def __init__(self,nume,prenume,anul_nasterii,luna_nasterii,ziua_nasterii,calificare="Manager"):
        super().__init__(nume,prenume,anul_nasterii,luna_nasterii,ziua_nasterii)
        self.calificare = calificare

    def adaugare_angajati(self):
        varsta_angajat=int(Fabrica.an_baza_de_date) - int(self.anul_nasterii)
        Emp = {
            "ID": self.ID,
            "nume": f"{self.nume} {self.prenume}",
            "email":self.email,
            "varsta_la_angajare":varsta_angajat,
            "functie/calificare":self.calificare,
            }
        read_json_file = open("Lista_angajati.json","r")
        convert_json_to_dict = json.load(read_json_file)
        read_json_file.close()
        poz = (len(convert_json_to_dict))
        convert_json_to_dict[poz + 1] = Emp
        new_angajat = json.dumps(convert_json_to_dict, indent=4)
        rewrite_json = open("Lista_angajati.json", "w")
        rewrite_json.write(new_angajat)
        rewrite_json.close()
        print("Angajatul a fost adaugat.\n")
    @staticmethod
    def eliminare_angajati():
        read_json_file = open("Lista_angajati.json", "r")
        convert_json_to_dict = json.load(read_json_file)
        read_json_file.close()
        j=0
        print("Lista angajatilor:")
        while j<len(convert_json_to_dict):
            for angajat in convert_json_to_dict:
                print(f"{j+1}. {convert_json_to_dict[angajat]['nume']}: ID - {convert_json_to_dict[angajat]['ID']}")
                j+=1
        print("0.  Revenire la meniul anterior")
        while True:
            ID_de_eliminat = input("Introduceti ID-ul angajatului pe care doriti sa il eliminati!\n>")
            if ID_de_eliminat == "0":
                break
            for angajat in convert_json_to_dict:
                if convert_json_to_dict[angajat]["ID"] == ID_de_eliminat:
                    pozitie = angajat
            optiune = int(input(f"Sunteti sigur ca vreti sa eliminati {convert_json_to_dict[pozitie]['nume']}, {convert_json_to_dict[pozitie]['ID']} din lista angajati?\n1. DA\n2. NU\n>"))
            try:
                if optiune==1:
                    convert_json_to_dict.pop(pozitie,"None")
                elif optiune==2:
                    break
                else:
                    print("Selectati o optiune valida!")
                    continue
            except:
                print("Selectati o optiune valida!")
                continue
    #creare nou dictionar pentru a pastra cheile consecutive
            new_Dict = dict()
            keys = []
            l=len(convert_json_to_dict)
            for i in range(0,l):
                keys.append(int(i)+1)
            lista_date = []
            for angajat in convert_json_to_dict.values():
                lista_date.append(angajat)
                lista_date.reverse()
            for key in keys:
                for val in lista_date:
                    new_Dict[key]=val
                lista_date.remove(val)

            new_angajat= json.dumps(new_Dict, indent=4)
            rewrite_json = open("Lista_angajati.json", "w")
            rewrite_json.write(new_angajat)
            rewrite_json.close()
            print("Angajatul a fost eliminat.\n\n0. Revenire la meniul anterior\nsau")
    @staticmethod
    def modificare_calificari():
        read_json_file = open("Lista_angajati.json", "r")
        convert_json_to_dict = json.load(read_json_file)
        read_json_file.close()
        print("Lista operatorilor este:\n")

        for angajat in convert_json_to_dict:
            if convert_json_to_dict[angajat]["functie/calificare"].lower()=="frigotehnist" or convert_json_to_dict[angajat]["functie/calificare"].lower()=="electronist" or convert_json_to_dict[angajat]["functie/calificare"].lower()== "instalator":
                print(f"{convert_json_to_dict[angajat]['nume']}, {convert_json_to_dict[angajat]['functie/calificare']}: ID - {convert_json_to_dict[angajat]['ID']}")
        print("0.  Revenire la meniul anterior")
        while True:
            ID_de_modificat = input("Introduceti ID-ul angajatului a carui calificare doriti sa o modificati\n>")
            if ID_de_modificat == "0":
                break
            calificare_noua=int(input("Selectati noua califica\n1. Frigotehnist\n2. Electronist\n3. Instalator\n>"))
            if calificare_noua == 1:
                calificare_noua ="Frigotehnist"
            elif calificare_noua ==2:
                calificare_noua="Electronist"
            else:
                calificare_noua="Instalator"

            for angajat in convert_json_to_dict:
                if convert_json_to_dict[angajat]["ID"] == ID_de_modificat:
                    convert_json_to_dict[angajat]["functie/calificare"]=calificare_noua
                    print(f"Calificarea a fost inlocuita cu noua calificare, {calificare_noua.lower()}.\n\n0. Revenire la meniul anterior\nsau")
            new_angajat = json.dumps(convert_json_to_dict, indent=4)
            rewrite_json = open("Lista_angajati.json", "w")
            rewrite_json.write(new_angajat)
            rewrite_json.close()

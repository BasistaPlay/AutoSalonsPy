import os
import sys
from multiprocessing import connection
from turtle import update
from venv import create
from h11 import Connection
import pymysql
from config import host, user, pasword, db_name
import time


try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=pasword,
        database=db_name
    )
    print("Izdevas savienoties ar datubazi")
    print('#' * 24)


except Exception as ex:
    print("Neizdevās savienoties ar datubazi")
    print(ex)


def AddData():
    print("==============================")
    print("  PIEVIENOT DATUS AUTOSALONA")
    print("==============================")

    print("- 1 - Diler")
    print("- 2 - Car")
    print("- 3 - Klient")
    print("- 4 - Back")
    AddData = int(input("Ievadiet ko gribat pievienot:"))

    if AddData == 1:
        os.system("cls")
        Adrese = str(input("Lūdzu ievadiet dilera adresi:"))
        MasinasSkaits = int(input("Lūdzu ievadiet dīlera mašinas skaitu:"))

        with connection.cursor() as cursor:
            insert_query = f"INSERT INTO `Dilers` (Adrese, MasinasSkaits) VALUES ( '{Adrese}' ,  \
                {MasinasSkaits}  )"
            # salons.Adrese + "," + salons.MasinasSkaits + \

            cursor.execute(insert_query)
            connection.commit()
            print("Dati tika veiksmīgi pievienoti!!!")

            for x in range(5, 0, -1):
                time.sleep(1)
                print(f"Pēc {x} sekundēm Jūs pārmetīs uz menu!!! ")
                sys.stdout.write("\033[F")
            os.system("cls")
            main()

    elif AddData == 2:
        os.system("cls")
        Marka = str(input("Lūdzu ievadiet Mašīnas marku:"))
        MasinasNumurs = str(input("Lūdzu ievadiet mašīnas numuru:"))
        Klase = str(input("Lūdzu ievadiet mašīnas klasi:"))

        with connection.cursor() as cursor:
            insert_query = f"INSERT INTO `Car` (Marka, MasinasNumurs,Klase) VALUES ( '{Marka}' ,'{MasinasNumurs}' ,'{Klase}')"
            # salons.Adrese + "," + salons.MasinasSkaits + \

            cursor.execute(insert_query)
            connection.commit()
            print("Dati tika veiksmīgi pievienoti!!!")

        for x in range(5, 0, -1):
            time.sleep(1)
            print(f"Pēc {x} sekundēm Jūs pārmetīs uz menu!!! ")
            sys.stdout.write("\033[F")
        os.system("cls")
        main()

    elif AddData == 3:
        os.system("cls")
        PersonasKods = str(input("Lūdzu ievadiet lietotāja personas kodu:"))
        Vards = str(input("Lūdzu ievadiuet savu vārdu:"))
        Uzvards = str(input("Lūdzu ievadiuet savu Uzvārdu:"))
        talr = str(input("Lūdzu ievadiet savu telefona numur:"))

        with connection.cursor() as cursor:
            insert_query = f"INSERT INTO `Klient` (PersonasKods, Vards, Uzvards, talr) VALUES ( '{PersonasKods}', '{Vards}', '{Uzvards}', '{talr}')"
            # salons.Adrese + "," + salons.MasinasSkaits + \

            cursor.execute(insert_query)
            connection.commit()
            print("Dati tika veiksmīgi pievienoti!!!")

        for x in range(5, 0, -1):
            time.sleep(1)
            print(f"Pēc {x} sekundēm Jūs pārmetīs uz menu!!! ")
            sys.stdout.write("\033[F")
        os.system("cls")
        main()

    elif AddData == 4:
        os.system("cls")
        main()
    else:
        os.system('clear')
        print("Jus ievadijāt neeskistējošu režīmu!")
        AddData()


def ViewData():
    pass


def ModifyData():
    print("==============================")
    print("  REDIĢĒT DATUS AUTOSALONA")
    print("==============================")

    print("- 1 - Diler")
    print("- 2 - Car")
    print("- 3 - Klient")
    print("- 4 - Back")
    ModifyData = int(input("Ievadiet ko gribat pievienot:"))

    if ModifyData == 1:
        id = int(input("Kurus datus jūs gribat rediģēt? Kads ir viņu id?: "))
        Adrese = str(input("Uz kādu adresi jūs mainīsiet:"))
        MasinasSkaits = int(input("Cik tagad dilerim ir mašīnas:"))

        with connection.cursor() as cursor:
            update_query = f"UPDATE `Dilers` SET Adrese = '{Adrese}', MasinasSkaits = {MasinasSkaits} WHERE id = {id}"
            cursor.execute(update_query)
            connection.commit()
            print("Dati tika veiksmīgi rediģēti!!!")

            for x in range(5, 0, -1):
                time.sleep(1)
                print(f"Pēc {x} sekundēm Jūs pārmetīs uz menu!!! ")
                sys.stdout.write("\033[F")
            os.system("cls")
            main()

    if ModifyData == 2:
        os.system("cls")
        id = int(input("Kurus datus jūs gribat rediģēt? Kads ir viņu id?: "))
        Marka = str(input("Lūdzu ievadiet jauno Mašīnas marku:"))
        MasinasNumurs = str(input("Lūdzu ievadiet jauno mašīnas numuru:"))
        Klase = str(input("Lūdzu ievadiet jauno mašīnas klasi:"))

        with connection.cursor() as cursor:
            update_query = f"UPDATE `Car` SET Marka = '{Marka}', MasinasNumurs = '{MasinasNumurs}',Klase = '{Klase}' WHERE id = {id}"
            cursor.execute(update_query)
            connection.commit()
            os.system("cls")
            print("Dati tika veiksmīgi rediģēti!!!")

            for x in range(5, 0, -1):
                time.sleep(1)
                print(f"Pēc {x} sekundēm Jūs pārmetīs uz menu!!! ")
                sys.stdout.write("\033[F")
            os.system("cls")
            main()

    if ModifyData == 3:
        os.system("cls")
        PersonasKods = str(input("Lūdzu ievadiet lietotāja personas kodu:"))
        Vards = str(input("Lūdzu ievadiuet savu vārdu:"))
        Uzvards = str(input("Lūdzu ievadiuet savu Uzvārdu:"))
        talr = str(input("Lūdzu ievadiet savu telefona numur:"))

        with connection.cursor() as cursor:
            update_query = f"UPDATE `Klient` SET PersonasKods = '{PersonasKods}', Vards = '{Vards}', Uzvards = '{Uzvards}',talr = '{talr}' WHERE PersonasKods = '{PersonasKods}'"
            cursor.execute(update_query)
            connection.commit()
            os.system("cls")
            print("Dati tika veiksmīgi rediģēti!!!")

            for x in range(5, 0, -1):
                time.sleep(1)
                print(f"Pēc {x} sekundēm Jūs pārmetīs uz menu!!! ")
                sys.stdout.write("\033[F")
            os.system("cls")
            main()

    elif ModifyData == 4:
        os.system("cls")
        main()
    else:
        os.system('clear')
        print("Jus ievadijāt neeskistējošu režīmu!")
        ModifyData()


def SearchData():
    pass


def Summary():
    pass


def Delete():
    print("==============================")
    print("    DZĒST DATUS AUTOSALONA")
    print("==============================")

    print("- 1 - Diler")
    print("- 2 - Car")
    print("- 3 - Klient")
    print("- 4 - Back")
    Delete = int(input("Ievadiet ko gribat pievienot:"))

    if Delete == 1:
        id = int(input("Kurus Datus jūs velaties izdzēst? Uzrakstat viņu id: "))

        with connection.cursor() as cursor:
            delete_query = f"DELETE FROM `Dilers` WHERE id = {id};"
            cursor.execute(delete_query)
            connection.commit()
            print("Dati tika veiksmīgi dzēsti!!!")

        for x in range(5, 0, -1):
            time.sleep(1)
            print(f"Pēc {x} sekundēm Jūs pārmetīs uz menu!!! ")
            sys.stdout.write("\033[F")

        os.system("cls")
        main()

    if Delete == 2:

        id = int(input("Kurus Datus jūs velaties izdzēst? Uzrakstat viņu id: "))

        with connection.cursor() as cursor:
            delete_query = f"DELETE FROM `Car` WHERE id = {id};"
            cursor.execute(delete_query)
            connection.commit()
            print("Dati tika veiksmīgi dzēsti!!!")

        for x in range(5, 0, -1):
            time.sleep(1)
            print(f"Pēc {x} sekundēm Jūs pārmetīs uz menu!!! ")
            sys.stdout.write("\033[F")

        os.system("cls")
        main()

    if Delete == 3:

        PersonasKods = int(
            input("Kurus Datus jūs velaties izdzēst? Uzrakstat viņu personaskodu: "))

        with connection.cursor() as cursor:
            delete_query = f"DELETE FROM `Klient` WHERE PersonasKods = '{PersonasKods}';"
            cursor.execute(delete_query)
            connection.commit()
            print("Dati tika veiksmīgi dzēsti!!!")

        for x in range(5, 0, -1):
            time.sleep(1)
            print(f"Pēc {x} sekundēm Jūs pārmetīs uz menu!!! ")
            sys.stdout.write("\033[F")

        os.system("cls")
        main()

    elif Delete == 4:
        os.system("cls")
        main()
    else:
        os.system('clear')
        print("Jus ievadijāt neeskistējošu režīmu!")
        AddData()


def main():
    print("========================")
    print("       AUTOSALONS")
    print("========================")
    print("- 1 - Add data")
    print("- 2 - View data")
    print("- 3 - Modify data")
    print("- 4 - Search data")
    print("- 5 - Summary")
    print("- 6 - Delete")
    print("- 7 - Exit")

    main = int(input("izvēlaties režīmu:"))

    if main == 1:
        os.system("cls")
        AddData()
    elif main == 2:
        os.system("cls")
        ViewData()
    elif main == 3:
        os.system("cls")
        ModifyData()
    elif main == 4:
        os.system("cls")
        SearchData()
    elif main == 5:
        os.system("cls")
        Summary()
    elif main == 6:
        os.system("cls")
        Delete()
    elif main == 7:
        os.system("cls")
    else:
        os.system('clear')
        print("Jus ievadijāt neeskistējošu režīmu!")


main()

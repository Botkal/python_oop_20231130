from abc import ABC, abstractmethod


class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def info(self):
        pass


class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, kenyelmi_szint):
        super().__init__(ar, szobaszam)
        self.kenyelmi_szint = kenyelmi_szint

    def info(self):
        return f"Egyágyas szoba #{self.szobaszam} - Ár: {self.ar} Ft, Kényelmi szint: {self.kenyelmi_szint}"


class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, kilatas):
        super().__init__(ar, szobaszam)
        self.kilatas = kilatas

    def info(self):
        return f"Kétágyas szoba #{self.szobaszam} - Ár: {self.ar} Ft, Kilátás: {self.kilatas}"


from datetime import date


class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def info(self):
        return f"Foglalás a {self.szoba.info()} számú szobára a következő napra: {self.datum}"


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def get_szobak_info(self):
        szobak_info = [szoba.info() for szoba in self.szobak]
        return "\n".join(szobak_info)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return foglalas

    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            return f"Foglalás lemondva: {foglalas.info()}"
        else:
            return "A megadott foglalás nem található."

    def listaz_foglalasok(self):
        foglalasok_info = [foglalas.info() for foglalas in self.foglalasok]
        return "\n".join(foglalasok_info)


def main(szalloda=None):
    szalloda = Szalloda("Wellness Hotel")

    szoba01 = EgyagyasSzoba(5000, 101, "Magas")
    szoba02 = KetagyasSzoba(8000, 102, "Tengerre néző")
    szoba03 = KetagyasSzoba(8000, 103, "Tengerre néző")

    szalloda.add_szoba(szoba01)
    szalloda.add_szoba(szoba02)
    szalloda.add_szoba(szoba03)

    foglalas01 = szalloda.foglalas(101, date(2023, 12, 1))
    foglalas02 = szalloda.foglalas(102, date(2023, 12, 1))
    foglalas03 = szalloda.foglalas(103, date(2023, 12, 1))
    foglalas04 = szalloda.foglalas(102, date(2023, 12, 2))
    foglalas05 = szalloda.foglalas(101, date(2023, 12, 2))


    while True:
        print("\nVálassz egy műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("0. Kilépés")

        valasztas = input("Választásod: ")

        if valasztas == "1":
            szalloda.get_szobak_info()
            szobaszam = input("Adja meg a foglalni kívánt szoba számát: ")
            datum = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            datum_obj = date.fromisoformat(datum)
            foglalas = szalloda.foglalas(int(szobaszam), datum_obj)
            print(f"Foglalás elkészült: {foglalas.info()}")

        elif valasztas == "2":
            foglalasok_info = szalloda.listaz_foglalasok()
            print("Jelenlegi foglalások:")
            print(foglalasok_info)

            lemondas_szobaszam = input("Adja meg a lemondani kívánt foglalás szoba számát: ")
            lemondas_datum = input("Adja meg a lemondani kívánt foglalás dátumát (YYYY-MM-DD formátumban): ")
            lemondas_datum_obj = date.fromisoformat(lemondas_datum)

            for foglalas in szalloda.foglalasok:
                if foglalas.szoba.szobaszam == int(lemondas_szobaszam) and foglalas.datum == lemondas_datum_obj:
                    szalloda.lemondas(foglalas)
                    print(f"Foglalás lemondva: {foglalas.info()}")
                    break
            else:
                print("A megadott foglalás nem található.")

        elif valasztas == "3":
            foglalasok_info = szalloda.listaz_foglalasok()
            print("Jelenlegi foglalások:")
            print(foglalasok_info)

        elif valasztas == "0":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás. Kérlek válassz más opciót!")


if __name__ == "__main__":
    main()

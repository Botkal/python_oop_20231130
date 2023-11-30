from abc import ABC, abstractmethod
from datetime import date


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


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def get_szobak_info(self):
        szobak_info = [szoba.info() for szoba in self.szobak]
        return "\n".join(szobak_info)


class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def info(self):
        return f"Foglalás a(z) {self.szoba.info()} szobára a következő napra: {self.datum}"


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def get_szobak_info(self):
        szobak_info = [szoba.info() for szoba in self.szobak]
        return "\n".join(szobak_info)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalas(szoba, datum)
                return foglalas


class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def info(self):
        return f"Foglalás a {self.szoba.info()} számú szobára a következő napra: {self.datum}"


class Lemondas:
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

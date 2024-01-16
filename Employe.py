from abc import ABC, abstractmethod
from datetime import datetime
from IR import IR
from IEmploye import IEmploye

class Employe(IR, IEmploye):
    _mtle_counter = 1

    def __init__(self, nom, dateNaissance, dateEmbauche, salaireBase):
        self._mtle = Employe._mtle_counter
        Employe._mtle_counter += 1
        self._nom = nom
        self._dateNaissance = dateNaissance
        self.DateEmbauche = dateEmbauche  
        self._salaireBase = salaireBase

    @property
    def DateEmbauche(self):
        return self._dateEmbauche

    @DateEmbauche.setter
    def DateEmbauche(self, value):
        if self.Age(value) < 20:
            raise ValueError("L'age de l'employe a la date d'embauche ne peut pas etre inferieur a 20 ans.")
        self._dateEmbauche = value

    @property
    def DateNaissance(self):
        return self._dateNaissance

    @abstractmethod
    def SalaireAPayer(self):
        pass

    def Age(self, date_reference=None):
        if date_reference is None:
            date_reference = datetime.now()
        return date_reference.year - self._dateNaissance.year - ((date_reference.month, date_reference.day) < (self._dateNaissance.month, self._dateNaissance.day))

    def Anciennete(self):
        return datetime.now().year - self._dateEmbauche.year

    def DateRetraite(self, ageRetraite):
        return self._dateNaissance.replace(year=self._dateNaissance.year + ageRetraite)

    def __str__(self):
        return f"{self._mtle}-{self._nom}-{self._dateNaissance}-{self._dateEmbauche}-{self._salaireBase}"

    def __eq__(self, other):
        return self._mtle == other._mtle
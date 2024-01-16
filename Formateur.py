from IR import IR
import Employe 


class Formateur(Employe):
    def __init__(self, nom, dateNaissance, dateEmbauche, salaireBase, heureSup=0, remunerationHSup=70.0):
        super().__init__(nom, dateNaissance, dateEmbauche, salaireBase)
        self._heureSup = heureSup
        self._remunerationHSup = remunerationHSup

    @property
    def RemunerationHSup(self):
        return self._remunerationHSup

    def SalaireAPayer(self):
        salaire_brut = (self._salaireBase + self._heureSup * self._remunerationHSup)
        taux_IR = self.getIR(salaire_brut)
        salaire_net = salaire_brut * (1 - taux_IR)
        return salaire_net

    def __str__(self):
        return f"{super().__str__()}-{self._heureSup}-{self._remunerationHSup}"

class Agent(Employe):
    def __init__(self, nom, dateNaissance, dateEmbauche, salaireBase, primeResponsabilite=0):
        super().__init__(nom, dateNaissance, dateEmbauche, salaireBase)
        self._primeResponsabilite = primeResponsabilite

    def SalaireAPayer(self):
        salaire_brut = self._salaireBase + self._primeResponsabilite
        taux_IR = self.getIR(salaire_brut)
        salaire_net = salaire_brut * (1 - taux_IR)
        return salaire_net

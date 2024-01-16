from abc import ABC, abstractmethod 

class IR(ABC):
    _tranches = [0, 30000, 50000, 60000, 80000, 180000]
    _tauxIR = [0, 0.1, 0.2, 0.3, 0.34, 0.38]

    @staticmethod
    def getIR(salaire):
        for i in range(len(IR._tranches)):
            if salaire <= IR._tranches[i]:
                return IR._tauxIR[i]

class IEmploye(ABC):
    @abstractmethod
    def Age(self):
        pass

    @abstractmethod
    def Anciennete(self):
        pass

    @abstractmethod
    def DateRetraite(self, ageRetraite):
        pass




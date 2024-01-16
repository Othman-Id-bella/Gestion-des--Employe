import IR
import Employe
import Formateur
import Agent



employe1 = Formateur("Ahmed", "1980", "2010", 50000, 10)
employe2 = Agent("Mohcine", "1985", "2015", 60000, 5000)
employe3 = Employe("Omar", "1990", "2020", 70000)

print(employe1.__str__())  
print(employe1.SalaireAPayer())
print(employe2.__str__())  
print(employe2.SalaireAPayer() )
print(employe3.__str__())  
print(employe3.SalaireAPayer())
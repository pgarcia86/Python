##  Modules

from my_module import sum, rest             ##  Del modulo my_module importo solamente las funciones definidas como sum y como rest

import other_module                         ##  Importo completa el modulo other_module con todos sus metodos


print(sum(4, 7))

print(rest(7, 4))

##print(prod(7, a))                           ##  Esta importacion da error porque solamente estamos importando sum y rest

print(other_module.otherSum(4, 7))

print(other_module.otherRest(7, 4))

print(other_module.otherProd(7, 4))

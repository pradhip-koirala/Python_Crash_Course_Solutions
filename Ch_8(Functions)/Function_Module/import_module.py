
#importing specific module
import module as md #importing module given alias

#importing specific function from module given alias
from module import make_pizza as mp

#importing all functions in a module
from module import *



md.make_pizza(16,'pepperoni')
md.make_pizza(12,'mushrooms','green peppers','extra cheese')


mp(14,'pepperoni','mushrooms','extra cheese')

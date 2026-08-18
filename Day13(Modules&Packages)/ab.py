#Approach 1 :
import a
import b

# aobj=a.Animal()
# aobj.display()
#
# bobj=b.Bird()
# bobj.display()


#Approach 2:
# from a import Animal
# from b import Bird

#if a & b modules has multiple classes then we use '*' symbol

from a import *
from b import *

aobj=a.Animal()
aobj.display()

bobj=b.Bird()
bobj.display()
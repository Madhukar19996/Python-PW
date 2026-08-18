import sys
sys.path.append("C:/Python-PW/Day13(Modules&Packages)/pack1")
sys.path.append("C:/Python-PW/Day13(Modules&Packages)/pack1/pack2")
#Approach 1 :


import module1
import module2

module1 .display()
module2 .show()

#Approach 2 :

from packaging.pylock import Package
# from.pack1.module1 import *
# from pack1.module2 import *
#
# display()
# show()


#Approach 3 : If module1 and module2 has common functions.

# from pack1.module1 import *
# display()

# from pack1.module2 import *
# show()
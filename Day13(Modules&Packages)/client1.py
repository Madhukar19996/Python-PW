#Approach 1 :


import pack1.module2

pack1.module1 .display()
pack1.module2 .show()

#Approach 2 :

# from pack1.module1 import *
# from pack1.module2 import *
#
# display()
# show()


#Approach 3 : If module1 and module2 has common functions.

# from pack1.module1 import *
# display()

# from pack1.module2 import *
# show()
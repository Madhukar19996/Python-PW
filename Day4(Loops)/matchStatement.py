#The match statement is used to perform different actions based on different conditions .
#Instead of writing many if ..else statements ,you can use the match statement.

#Example 1 :

# day=7
# match day :
#     case 1 :
#        print("sunday")
#     case 2:
#         print("monday")
#     case 3:
#         print("tuesday")
#     case 4:
#         print("wednesday")
#     case 5:
#         print("thursday")
#     case 6:
#         print("friday")
#     case 7:
#         print("saturday")
#     case _:
#         print("invalid week day")


#Example 2 : combine values
# day=5
# match day:
#    case 1 | 7 :print("weekend")
#    case 2 | 3| 4 | 5 | 6 :print("weekday")
#    case _:print("invalid weekday")




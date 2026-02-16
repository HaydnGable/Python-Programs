from collections import OrderedDict
plain = {'a':1,
'b':2,
'c':3
}
print(plain)
fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(fancy)
#Yes, the OrderedDict fancy printed in the same order as the plain dictionary
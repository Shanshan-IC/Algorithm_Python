# copy list
a = [1, 2, 3, 4]
b = list(a)

# create a list with same value
same = [ 0 for i in xrange(5 + 1)]

# sort a list
a.sort()

#remove duplicate
a = list(set(a))

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sort a dict by key
import collections
od = collections.OrderedDict(sorted(x.items()))
# sort a dict by value
import operator
sorted_x = sorted(x.items(), key=operator.itemgetter(1))

# compare difference in a list
[j-i for i, j in zip(a[:-1], a[1:])]
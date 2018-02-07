arr = [9,4,2,1,55,3,2,1]

print "[] - Array "
print arr

print "len()"
print len(arr)

print "append() to array"
arr.append(33)
print arr

print "remove() from array"
arr.remove(33)
print arr

print "del - remove by index"
del arr[1]
print arr

print "pop() - remove item from end of array"
item = arr.pop()
print item
print arr

print "combine arrays with +/-"
arr2 = [55,66]
print(arr + arr2)

print "slice()"
print arr[1:3]
print arr[:3]
print arr[-3]
print arr[:-3]

print "sort()"
arr.sort()
print arr

print "reverse()"
arr2 = [3,2,1,5,6]
arr2.reverse()
print arr2

print "index()"
print arr.index(2)
print arr.index(9)

#second problem 
"""You have a two-dimensional list in the following format:
data = [[2, 5], [3, 4], [8, 7]]
Each sub-list contains two items, and each item in the sub-lists is an integer.
Write a function processData() that processes each sub-list like so:
[2, 5] --> 2 - 5 --> -3
[3, 4] --> 3 - 4 --> -1
[8, 7] --> 8 - 7 --> 1
and then returns the product of all the processed sub-lists: -3 * -1 * 1 = 3."""
data = [[2,5],[3,4],[8,7]]
def processData(data):
    x = data[0][0]-data[0][1]
    y = data[1][0]-data[1][1]
    z = data [2][0]-data[2][1]
    product = x * y * z 
    return product 
print("The product of all the processed sub-list: {}".format(processData(data))) 

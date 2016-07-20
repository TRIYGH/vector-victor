# W2D3

def shape(shape_list):
    if len(shape_list) == 1:
        tup_shape = (len(shape_list), )
    else:
        tup_shape = (len(shape_list), )
    return tup_shape


def vector_add(list1, list2):
    zip_the_list = []
    if shape(list1) == shape(list2):
        zip_the_list = [x+y for x,y in zip(list1, list2)]
        return zip_the_list


def vector_sub(list1, list2):
    zip_the_list = []
    if shape(list1) == shape(list2):
        zip_the_list = [x-y for x,y in zip(list1, list2)]
        return zip_the_list


# m = [3, 4]
# n = [5, 0]
#
# v = [1, 3, 0]
# w = [0, 2, 4]
# u = [1, 1, 1]
# y = [10, 20, 30]
# z = [0, 0, 0]
#
# print(list(vector_add(v,w))

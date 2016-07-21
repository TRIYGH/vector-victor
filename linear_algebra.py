# W2D3

def shape(shape_list):
    if len(shape_list) == 1:
        tup_shape = (len(shape_list), )
    else:
        tup_shape = (len(shape_list), )
    return tup_shape


def vector_add(list1, list2):
    zip_the_list = []
    if vector_size_equal(list1, list2):           #if shape(list1) == shape(list2):
        zip_the_list = [x+y for x,y in zip(list1, list2)]
        return zip_the_list
    else:
        raise ShapeError


def vector_sub(list1, list2):
    zip_the_list = []
    if shape(list1) == shape(list2):
        zip_the_list = [x-y for x,y in zip(list1, list2)]
        return zip_the_list
    else:
        raise ShapeError


def vector_sum(*lists):
    zip_the_list = []
    if vector_size_equal(*lists):
        zip_the_list = [sum(arg) for arg in zip(*lists)]
        return zip_the_list
    else:
        raise ShapeError

#ANSWER  ==  return len(set([shape(item) for item in args])) == 1



def vector_size_equal(*vectors):
    temp_str = ""
    for each in vectors:
        temp_str += str(len(each))
    eq = list(temp_str)[0]
    for each in list(temp_str):
        if each != eq:
            return False
    return True


def dot(a,b):
    if vector_size_equal(a,b):
        zip_the_list = [x*y for x,y in zip(a,b)]
        total = sum(zip_the_list)
        return total
    else:
        raise ShapeError


def vector_multiply(vector, num):
    zip_the_list = [x * num for x in vector]
    return zip_the_list


def vector_mean(*vectors):
    zip_the_list = [sum(args)/len(args) for args in zip(*vectors)]
    return zip_the_list


m = [3, 4]
n = [5, 0]

v = [1, 3, 0]
w = [0, 2, 4]
u = [1, 1, 1]
y = [10, 20, 30]
z = [0, 0, 0]

a = [1,2,3]
b=[3,3,3]

print(vector_mean(v,w,u)[0])

class ShapeError(Exception):
    pass

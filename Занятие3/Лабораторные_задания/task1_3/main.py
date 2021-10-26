def simple_list(n):
    list_ = []
    z = 2
    if n == 1:
        return list_
    if n/2 == 0:
        return simple_list(n//z, z, list+[z])
    else:
        return simple_list(n,z+1, list)

if __name__ == "__main__":
    print (simple_list(568))


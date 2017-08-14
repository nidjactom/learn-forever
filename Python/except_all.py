def all_far(x, y):
    z=x/y
    return z

def all_close(x, y):
    try:
        print('Calculating %s/%s' %(x,y))
        z=x/y
    except BaseException as exception:
        print('Unexpected error ->', str(exception))

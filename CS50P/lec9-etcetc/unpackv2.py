# unpack using *args and **kwargs - enable functions to take in a variable number of arguments kwargs - keyword arguments aka named parameters
# the names *args and **kwargs is a convention and can be anything you want
# you can pass both to other functions
def f(*args, **kwargs):
    print("Positional:", kwargs)

#f(100, 50, 25)
f(galleons=100, sickles=50, knuts=25)

#print review
#print(*objects, sep=' ', end='\n',file=sys.stdout, flush=False)
# *objects - print takes a variable number of arguments, including none


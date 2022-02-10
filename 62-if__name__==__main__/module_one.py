# if __name__ == '__main__'
#
# Python interpreter sets "special variables", one of which is __name__
# Python will assign the __name__variable a value of "__main__" if it is
# The initial module being run

def hello():
    print("Hello!")

if __name__ == "__main__":
    print("running this module directly")
    hello()
else:
    print("running this other module indirectly")





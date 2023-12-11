def scope_test():
    def do_local():
        spam = "local spam"  # the local assignment doesn't affect the outer scope.

    def do_nonlocal():
        nonlocal spam  #Uses the nonlocal keyword to indicate that it wants to modify the spam variable from the nearest enclosing scope (scope_test function).
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()                               #it indicates that you want to modify a variable from the global scope, not a local one.. 
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
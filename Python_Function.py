'''
*** what is Function ***
Ans: A function is a block of code which only runs when it is called.
    You can pass data, known as parameters, into a function.
    A function can return data as a result.
    
Creating a Function :-
    In Python a function is defined using the def keyword:    
    Example:
        def my_function():
            print("Hello from a function")
        my_function()

***  Arguments  ***

Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. 
You can add as many arguments as you want, just separate them with a comma.
The following example has a function with one argument (fname). When the function is called, 
we pass along a first name, which is used inside the function to print the full name:
        
    def my_function(fname):
        print(fname + " Nagar")

    my_function("Jagdish")
    my_function("Sumit")
    my_function("Naveen")

Parameters or Arguments ?
The terms parameter and argument can be used for the same thing: 
    information that are passed into a function.

From a function's perspective :-
    A parameter is the variable listed inside the parentheses in the function definition.
    An argument is the value that is sent to the function when it is called.

Number of Arguments :-
    By default, a function must be called with the correct number of arguments. 
    Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, 
    not more, and not less.

Example :-
This function expects 2 arguments, and gets 2 arguments:
    def my_function(fname, lname):
      print(fname + " " + lname)
    
    my_function("Jagdish", "Nagar")

This function expects 2 arguments, but gets only 1: 
    def my_function(fname, lname):
      print(fname + " " + lname)
    
    my_function("Jagdish")

    
Arbitrary Arguments, *args :-
    If you do not know how many arguments that will be passed into your function, 
    add a * before the parameter name in the function definition.
    
    def my_function(*name):
        print("The youngest is " + name[2])
    
    my_function("Jagdish", "Naveen", "Sumit")

Keyword Arguments :-
    You can also send arguments with the key = value syntax.
    This way the order of the arguments does not matter.

Example:-
    def my_function(child3, child2, child1):
        print("The youngest is " + child2)

    my_function(child1 = "Jagdish", child2 = "Sumit", child3 = "Naveen")


Arbitrary Keyword Arguments, **kwargs :-
    If you do not know how many keyword arguments that will be passed into your function, add two asterisk: 
    ** before the parameter name in the function definition.
    This way the function will receive a dictionary of arguments, and can access the items accordingly:

Example :-
    def my_function(**kid):
        print("His last name is " + kid["lname"])
    my_function(fname = "Jagdish lname = "Nagar")


Default Parameter Value :-
The following example shows how to use a default parameter value.
If we call the function without argument, it uses the default value:

Example :-
    def my_function(country = "India"):
        print("I am from " + country)
    my_function()
    my_function("Swedwn")
    my_function("Norway")
    my_function("Brazil")

Passing a List as an Argument :-
    You can send any data types of argument to a function (string, number, list, dictionary etc.), 
    and it will be treated as the same data type inside the function.

    Example:
    def my_function(food):
        for x in food:
        print(x)
    fruits = ["apple", "banana", "cherry"]
    my_function(fruits)

    
Return Values :-
    To let a function return a value, use the return statement:
    Example:
    def my_function(x):
        return 5 * x
        print(my_function(3))
        print(my_function(5))
        print(my_function(9))


The pass Statement :-
    function definitions cannot be empty, but if you for some reason have a 
    function definition with no content, put in the pass statement to avoid getting an error.

    def myfunction():
        pass
    
    # having an empty function definition like this, would raise an error without the pass statement


Recursion :-
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. 

This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip 
into writing a function which never terminates, or one that uses excess amounts of memory or 
processor power. However, when written correctly recursion can be a very efficient and 
mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). 
We use the k variable as the data, which decrements (-1) every time we recurse. 
The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, 
best way to find out is by testing and modifying it.

    Example:-
    def recursion(k):
    if(k > 0):
        result = k + recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

    print("\n\nRecursion Example Results")
    recursion(6)

    '''
size = 5

def cone(size):

    x = 1
    while x <= size:
        space = (size - x) +1 
        cone = (" " * space) + ("/" * x) + "**" + ("\\" * x) 
        print(cone)
        x = x + 1
    
square = ("=*" * (size + 1))
bar = "+" + sqaure + "+"

uptri = "/\\"
downtri = "\\/"

multiple = 2
length = len(bar) #scaling the length of the bar to the length of the first layer
first_layer_dot = ("." * ((length - 6)/2))

first_layer = "|" + ((first_layer_dot + uptri + first_layer_dot) * 2) + "|"
second_layer = "|" + 

cone(size)
print(bar)


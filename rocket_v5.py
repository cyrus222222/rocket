size = int(input("size of rocket:"))
while size >= 20:
    print("enter a different number")
    size = int(input("size of rocket:"))

def stage_up():
    for i in range (1, size + 1):
        print("|"
              + '.' * (size - i)
              + ("/\\" * i)
              + "." * (2 * (size - i))
              + "/\\" * i
              + "." * (size - i)
              + "|")


def stage_down():
    for i in range (0, size):
        print("|"
            + '.' * (i)
            + ("\\/" * (size - i))
            + "." * (2 * (i))
            + ("\\/" * (size - i))
            + "." * (i)
            + "|")

def divider():
    print("+" + ("=*" * 2 * size) + "+")

def cone():
    for i in range (1, 2* (size)):
        print(" " * (2 * size - i)
              + ("/" * i)
              + "**"
              + ("\\" * i))

cone()
divider()
stage_up()
stage_down()
divider()
stage_down()
stage_up()
divider()
cone()

size = 5

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

stage_up()
stage_down()

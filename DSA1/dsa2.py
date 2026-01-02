import sys

QUIET = '--quiet' in sys.argv or '-q' in sys.argv

def p(*args, **kwargs):
    if not QUIET:
        print(*args, **kwargs)


def main():
    try:
        p(5)
    except:
        p("it is a number")


    A = ["vxhgfsqx", "uvx", "sqf"]
    p(A)

    A.remove("uvx")
    p("update list: \n", A)

    A = ["vxhgfsqx", "uvx", "sqf"]
    b = list(A)
    b.remove("uvx")
    p(b)

    A = ["vxhgfsqx", "uvx", "sqf"]
    b = list(A)
    b.append("hiejvieg")
    p(b)

    A = {"vxhgfsqx", "uvx", "sqf"}
    A.add("hdsgvi")
    p(A)

    A = {"vxhgfsqx", "uvx", "sqf"}
    b = {"jsgdqvs", "kosqdg", "duhtd"}
    A.update(b)
    p(A)

    thislist = ["name", "age", "pot", "city"]
    p(thislist)

    thislist.remove("name")
    thislist.remove("pot")

    p("updatw List: \n", thislist)

    thislist = {"name", "age", "pot", "city"}
    p(thislist)

    thislist.remove("city")
    thislist.remove("pot")

    p("updatw List: \n", thislist)

    thislist = ("name", "age", "pot", "city")
    p(thislist)

    thislist = ["name", "age", "pot", "city"]
    p(thislist)

    thislist.pop(2)

    p("update list: \n", thislist)

    thislist = ["name", "age", "pot", "city"]
    p(thislist)

    thislist.pop()

    p("update list: \n", thislist)

    thislist = ["name", "age", "pot", "city"]
    p(thislist)

    thislist.clear()

    p("update list: \n", thislist)

    thislist = ["name", "age", "pot", "city"]
    p(thislist)

    del thislist[1]
    p("update list: \n", thislist)

    for i in range(1, 11):
        p(i)

    for i in range(1, 6):
        p(i**2)

    num = i
    for i in range(1, num + 1):
        if i == 50:
            break
        p(i*2)


if __name__ == '__main__':
    main()

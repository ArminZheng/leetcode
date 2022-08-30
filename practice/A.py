def aaa():
    print("you're idiot!")


if __name__ == '__main__':
    # description
    print(__name__)
    print(aaa.__doc__)
    print(aaa.__annotations__)
else:
    print("hah")
    print(__name__)

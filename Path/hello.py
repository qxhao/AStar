import sys

if __name__ == "__main__":
    for i in range(0, len(sys.argv), 1):
        print("参数%d:" % i, sys.argv[i], sep=' ')
    print("hello.")
    sys.exit(0)
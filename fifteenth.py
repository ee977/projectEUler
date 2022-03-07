import math
def main():
    grid = 20
    routes = math.factorial(grid*2) / (math.factorial(grid)**2)
    print(routes)

if __name__ == '__main__':
    main()
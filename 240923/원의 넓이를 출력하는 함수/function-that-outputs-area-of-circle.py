import sys

N = int(sys.stdin.readline())

result = N*N*3.14
formatted_result = "{:.2f}".format(result)
print(formatted_result)
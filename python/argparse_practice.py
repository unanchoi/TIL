import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name", help="Write yourname!")
parser.add_argument("age", help = "Write your age!", type=int)
parser.add_argument("job", help = "Write your job")
arg = parser.parse_args()

print(arg.name, arg.age - 1, arg.job)

'''
Option Argument
'''

parser2 = argparse.ArgumentParser()
parser2.add_argument("--brain", help="brain", action="store_true")

args2 = parser.parse_args()
if args2.brain:
    print("you are genius!")

## References
# https://supermemi.tistory.com/entry/%EB%A8%B8%EC%8B%A0-%EB%9F%AC%EB%8B%9D-%EB%AA%A8%EB%8D%B8%EC%97%90%EC%84%9C-argparse-%EC%82%AC%EC%9A%A9-%EB%B0%A9%EB%B2%95-%EC%98%88%EC%A0%9C

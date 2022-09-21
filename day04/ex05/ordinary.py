import sys
import psutil

def function():
    file = sys.argv[1]
    with open(file) as f:
        for line in f:
            return line

def main():
    for el in function():
        pass
    mem = psutil.Process().memory_info().vms/(10**9)
    cpu = psutil.Process().cpu_times()
    print(f'Peak Memory Usage = {mem} Gb')
    print(f'User Time + System Time = {cpu.user + cpu.system}s')

if __name__ == '__main__':
    try:
        main()
    except BaseException:
        print("ERROR")
import sys
from sample_numbers.node import Node

def main():
    argc = len(sys.argv)
    
    start = int(sys.argv[1][0]) if argc > 1 else 9
    end = int(sys.argv[2][0]) if argc > 2 else 0
    result = int(sys.argv[3]) if argc > 3 else 200

    node = Node(start)

    if start != end:
        step = 1 if start < end else -1

        for digit in range(start + step, end + step, step):
            node.append(digit)

    equations = node.find_equations(result)

    print(f'Equations with result of {result} and a dictionary from {start} to {end}:')
    print('\n'.join(equations))

if __name__ == '__main__':
    main()

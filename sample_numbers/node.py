class Node:

    def __init__(self, value: int):
        self.__next = None
        self.__value = value

    def __get_last(self):
        last_node = self

        while (node := last_node.__next):
            last_node = node

        return last_node

    def append(self, value: int):
        self.__get_last().__next = Node(value)

    def __modify_equation(self, equation: list,
                          left_value: int, right_value: int,
                          operator: str, modifier: callable):
        operator_result = modifier(left_value, self.__value)

        if (isinstance(operator_result, list)):
            equation += operator_result
        else:
            if (equation):
                equation[-1] = operator_result
            else:
                equation = [operator_result]

    def __equation_to_string(self, equation: list):
        string_equation = ''

        for value in equation:
            if (value >= 0) and (string_equation):
                string_equation += '+' + str(value)
            else:
                string_equation += str(value)

        return string_equation

    def find_equations(self, result: int, equation=None):
        OPERATORS = {
            '+': lambda left, right : [right],
            '-': lambda left, right : [-right],
            '': lambda left, right : left * 10 + right
        }

        if not equation:
            equation = []

        equation_len = len(equation)

        result_equations = set()

        left_value = equation[-1] if len(equation) > 0 else 0

        for operator, modifier in OPERATORS.items():
            self.__modify_equation(equation, left_value, self.__value,
                    operator, modifier)

            if (self.__next):
                result_equations = result_equations.union(
                        self.__next.find_equations(result, equation))
            else:
                if (sum(equation) == result):
                    result_equations.add(
                        self.__equation_to_string(equation))

            del equation[equation_len:]

        return result_equations

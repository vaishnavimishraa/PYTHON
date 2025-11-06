#Q10
def print_truth_table(operator):
    print(f"Truth Table for {operator._name_} Operator:")
    print("A\tB\tResult")
    print("----------------")
    for A in [0, 1]:
        for B in [0, 1]:
            result = operator(A, B)
            print(f"{A}\t{B}\t{result}")


print_truth_table(lambda a, b: a & b)


print_truth_table(lambda a, b: a | b)


print_truth_table(lambda a, b: a ^ b)


def arithmetic_arranger(problems, solutions=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    # Creating for empty strings for all the lines
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for i, problem in enumerate(problems):
        num1, op, num2 = problem.split()

        # Proper error handling
        if not op in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Performing operations as required
        if op == "+":
            solution = int(num1) + int(num2)
        else:
            solution = int(num1) - int(num2)

        # Setting the num_length to be large enough to hold the two nums
        num_length = len(max([num1, num2], key=len))

        line1 += num1.rjust(num_length + 2)
        line2 += op + num2.rjust(num_length + 1)
        line3 += "-" * (num_length + 2)
        line4 += str(solution).rjust(num_length + 2)

        # When i < len(problems - 1) the problem has displayed completely and moving to next problem
        if i < len(problems) - 1:
            line1 += "    "
            line2 += "    "
            line3 += "    "
            line4 += "    "

    vertical_problems = line1 + "\n" + line2 + "\n" + line3

    if solutions:
        vertical_problems += "\n" + line4

    return vertical_problems

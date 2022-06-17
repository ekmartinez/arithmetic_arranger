
def arithmetic_arranger(problems, display=False):

    if len(problems) > 5:
        return'Error: Too many problems.'

    line1, line2, line3, line4= "", "", "",""
    for indx, chars in enumerate(problems):
        operand1, operator, operand2 = chars.split()

        if len(operand1) > 4:
            return "Error: Numbers cannot be more than four digits."
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if operand1.isdigit() == False or operand2.isdigit() == False:
            return "Error: Numbers must only contain digits."

        if operator == '+':
            result = int(operand1) + int(operand2)
        elif operator == '-':
            result = int(operand1) - int(operand2)

        max_length = max(len(operand1), len(operand2))

        line1 = line1 + operand1.rjust(max_length+2)
        line2 = line2 + operator + operand2.rjust(max_length+1)
        line3 = line3 +  "-" * (max_length + 2)
        line4 = line4 + str(result).rjust(max_length+2)

        if indx < len(problems)-1:
            line1 = line1 + "    "
            line2 = line2 + "    "
            line3 = line3 + "    "
            line4 = line4 + "    "

        if display ==  True:
            arranged_problems = f'{line1}\n{line2}\n{line3}\n{line4}'
        else:
            arranged_problems = f'{line1}\n{line2}\n{line3}'

    return arranged_problems

print(arithmetic_arranger(['32 - 698', '422 + 56', '410 + 4333', '4444 - 444', '77 - 4'], True))



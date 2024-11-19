def add(num1, print_output=False, num2=0):
    answer = num1 + num2

    if print_output:
        print(answer)

    return answer


args = {
    'num1': 12,
    'num2': 10,
    'print_output': False
}

output = add(**args)
output = add(num1=args['num1'], num2=args['num2'],
             print_output=args['print_output'])

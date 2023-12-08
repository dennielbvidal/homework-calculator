import csv

def calculate(num1, operator, num2):
    try:
        if operator == '||':
            return str(num1) + str(num2)
        return {
            '+': float(num1) + float(num2),
            '-': float(num1) - float(num2),
            '*': float(num1) * float(num2),
            '/': float(num1) / float(num2) if float(num2) != 0 else 'Cannot divide by zero',
            }.get(operator, f'Invalid operator: {operator}')
    except Exception as e:
        return f'Error: {e} in row: {num1}, {operator}, {num2}'

with open('input.csv', 'r') as input_file, open('output_data.csv', 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(['ANSWER'])
    next(input_file)
    for row in csv.reader(input_file):
        result = calculate(*row)
        csv_writer.writerow([result]) if isinstance(result, (float, int, str)) else print(f'Invalid row: {row}, result: {result}')
print('COMPLETED')
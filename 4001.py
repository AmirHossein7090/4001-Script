class Error(BaseException):
    def __init__(self, message):
        self.msg = message

    def __str__(self):
        return self.msg


def get_variable_value(params: str) -> str:
    params = params.split('%')
    for i, item in enumerate(params):
        if item in variables.keys():
            params[i] = variables[item]
    return ''.join([str(item) for item in params if item])


def is_valid_variable(id_: str) -> bool:
    for char in id_:
        if char.isupper() or char.islower() or char.isnumeric() or '_' == char:
            continue
        else:
            return False
    return True


def is_prime(number: int) -> bool:
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True


def run_script(path: str):
    global run_from_file
    run_from_file = True
    with open(path, 'r') as file:
        scripts = file.read().split('\n')
        if not scripts[-1]:  # Checks for blank line
            scripts = scripts[:-1]
    for command in scripts:
        command = get_variable_value(command).split(':')
        print(command)
        if 'do' in command or ':' in command:
            command = ' '.join(command[1:])  # command[1:] === delete the ':' char
            continue
        # result = command_handler(command)
        # if result:
        #     print(result)
    run_from_file = False


def read_file(path: str):
    with open(path, 'r') as file:
        return file.read()


def file_writer(file_command: list):
    global file_object, file_path, file_opened
    if file_command[0] == 'open':
        file_object = open(file_path, 'w')
        print(f'File "{file_path}" opened')
        file_opened = True
    elif file_command[0] == 'close':
        file_object.close()
        file_opened = False
        print(f'File "{file_path}" closed')


def do(params: list):
    global run_from_file
    n = int(params[0])
    command = params[1:]
    all_commands = []
    response = []
    if not command:
        if not run_from_file:
            while True:
                command = input(': ')
                all_commands.append(command)
                if not command:
                    break
        for _ in range(n):
            for c in all_commands[:-1]:
                result = command_handler(c.split())
                if result:
                    response.append(result)
    else:
        for _ in range(n):
            response.append(command_handler(command))
    return '\n'.join([str(item) for item in response])


def primes(n: str):
    result = []
    for num in range(2, int(n) + 1):
        if is_prime(num):
            result.append(str(num))
    return ', '.join(result)


def get(params: list[str]):
    var = params[0]
    prompt = params[1]
    if not is_valid_variable(var):
        raise Error(f'The variable "{var}" is not valid!')
    try:
        var = str(var)
    except ValueError:
        raise ValueError('The expected parameter is the "str", but the "int" is entered')

    variables[var] = prompt
    return f'{var}={prompt}'


def calc(params: list[str]):
    operators = []
    numbers = []
    variable = False
    for i, item in enumerate(params):
        if i == 0 and item.isalpha():  # If there was a variable
            if not is_valid_variable(item):
                raise Error(f'The variable "{item}" is not valid!')
            try:
                variable = str(item)
            except ValueError:
                raise ValueError('The expected parameter is the "str", but the "int" is entered')
        elif variable and item.isnumeric() and i <= 1:
            if '.' in item:
                variables[params[0]] = float(item)
            variables[params[0]] = int(item)
            return
        elif item in '+-*/^#\\':
            operators.append(item)
        else:
            try:
                if '.' in item:
                    numbers.append(float(item))
                elif item:
                    numbers.append(int(item))
            except ValueError:
                raise ValueError('The expected parameter is the "int", but the "str" is entered')

    result = numbers[0]
    for operator, num in zip(operators[::-1], numbers[1:]):
        if operator == '+':
            result += num
        elif operator == '-':
            result -= num
        elif operator == '*':
            result *= num
        elif operator == '/':
            result /= num
        elif operator == '^':
            result **= num
        elif operator == '#':
            result %= num
        elif operator == '\\':
            result //= num
        else:
            raise Error(f"The operator \"{operator}\" does not defined")

    if variable:
        variables[variable] = result
    else:
        return result


def pause():
    input('Please press ENTER to continue...')


def echo(params: list[str]):
    return ' '.join(params)


def command_handler(command):
    global file_opened, file_path
    if command:
        match command:
            case ['echo', *_]:
                return echo(command[1:])
            case ['pause', *_]:
                pause()
            case ['calc', *_]:
                return calc(command[1:])
            case ['get', *_]:
                return get(command[1:])
            case ['prims', n]:
                return primes(n)
            case ['do', *_]:
                return do(command[1:])
            case ['open', *_]:
                file_path = ' '.join(command[1:])
                file_writer(command)
            case ['close']:
                file_writer(command)
            case ['read', *_]:  # read file test.txt ->  ['read', 'file', 'test.txt']
                path = ' '.join(command[1:])
                return read_file(path)
            case ['run', *_]:
                path = ' '.join(command[1:])
                run_script(path)
            case _:
                raise Error(f'"{command[0]}" function is not defined')


def main():
    global file_object, file_opened
    commands = input('> ')
    commands = get_variable_value(commands).split()
    command_result = command_handler(commands)
    if file_opened and command_result:
        if file_object.tell() == 0:
            file_object.write(str(command_result))
        else:
            file_object.write('\n' + str(command_result))
    return command_result


# Variables handler
variables = dict()
# File handler
file_opened = False
file_object = None
file_path = str()
# Run scripts handler
run_from_file = False
while True:
    m_result = main()
    if m_result:
        print(m_result)

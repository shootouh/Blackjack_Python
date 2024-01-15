NAMES = ['Johnny', 'Sol', 'Anji']

def get_input_with_validator(prompt, validator, error_message="Invalid input."):
    input_value = input(prompt)
    while not validator(input_value):
        print(error_message)
        input_value = input(prompt)
    return input_value
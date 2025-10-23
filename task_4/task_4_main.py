import inspect

from task_4.task_4_command_handlers import hello, add_contact, change_contact, show_phone, show_all, help_command, exit_bot
from task_4.task_4_custom_exceptions import ExitBot, InvalidCommand, NotFound

COMMANDS = {
    'hello': {'handler': hello, 'description': 'Greet the bot'},
    'add': {'handler': add_contact, 'description': 'Add a new contact: add [name] [phone]'},
    'change': {'handler': change_contact, 'description': "Change a contact's phone: change [name] [new_phone]"},
    'phone': {'handler': show_phone, 'description': "Show a contact by phone: phone [phone]"},
    'all': {'handler': show_all,  'description': 'Show all contacts'},
    'help': {'handler': help_command, 'description': 'Show this help message'},
    'exit': {'handler': exit_bot, 'description': 'Exit the program'},
    'close': {'handler': exit_bot, 'description': 'Exit the program'}
}

def main():
    contacts = {}

    print('Welcome to the assistant bot!')

    while True:
        try:
            user_input = input('Enter a command: ')

            if not user_input:
                continue

            print(_handle_user_input(user_input, contacts))

        except InvalidCommand as ic:
            print(ic)
            continue
        except NotFound as nf:
            print(nf)
        except ExitBot as eb:
            print(eb)
            break
        except Exception as ex:
            print(f'An error occurred: {ex}. Please try again.')
            break

def parse_input(user_input: str) -> tuple[str, list]:
    parts = user_input.split()
    command = parts[0].lower()
    arguments = parts[1:]
    return command, arguments

def _handle_user_input(user_input: str, contacts: dict) -> str:
    command, arguments = parse_input(user_input)

    if command not in COMMANDS:
        raise InvalidCommand('Invalid command')

    handler = COMMANDS[command]['handler']

    if command == 'help':
        return handler( _get_command_description_list())

    sig = inspect.signature(handler)
    param_count = len(sig.parameters)

    try:
        if param_count == 0:
            return handler()
        elif param_count == 1:
            return handler(contacts)
        elif param_count == 2:
            return handler(contacts, arguments)
        else:
            raise InvalidCommand("Invalid number of arguments for this command.")
    except TypeError:
        raise InvalidCommand("Invalid number of arguments for this command.")

def _get_command_description_list() -> list[str]:
    return [f"{cmd}: {body['description']}" for cmd, body in COMMANDS.items()]

if __name__ == "__main__":
    main()

from functools import wraps

from task_4.task_4_custom_exceptions import ExitBot, InvalidCommand, NotFound

def input_error(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except KeyError as ex:
            missing = str(ex).strip("'") if ex.args else "Unknown"
            raise NotFound(f"'{missing}' not found. Please check the name and try again.")

        except IndexError:
            raise InvalidCommand(
                "Invalid command format. It looks like you missed one or more arguments.\n"
                "Tip: Use 'help' to see how to use each command properly."
            )

        except ValueError:
            raise InvalidCommand(
                "Invalid data format. Please make sure you entered the correct number of arguments "
                "and separated them with spaces.\n"
                "Tip: Use 'help' to see how to use each command properly."
            )

        except TypeError:
            raise InvalidCommand(
                "This command was used incorrectly. Some arguments may be missing or extra.\n"
                "Tip: Use 'help' to see how to use each command properly."
            )
    return wrapper

@input_error
def add_contact(contacts: dict, arguments: list) -> str:
    name, phone = arguments
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(contacts: dict, arguments: list) -> str:
    name, new_phone = arguments
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        raise NotFound("Contact not found.")

@input_error
def show_phone(contacts: dict, arguments: list) -> str:
    name = arguments[0]
    if name in contacts:
        return contacts[name]
    else:
        raise NotFound(f"Contact '{name}' not found.")

@input_error
def show_all(contacts: dict) -> str:
    if not contacts:
        raise NotFound("No contacts found.")

    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def hello() -> str:
    return "How can I help you?"

def help_command(command_list: list[str]) -> str:
    if not command_list:
        raise NotFound("No available commands found.")
    return "Available commands:\n" + "\n".join(f" - {cmd}" for cmd in command_list)

def exit_bot() -> None:
    raise ExitBot("Good bye!")
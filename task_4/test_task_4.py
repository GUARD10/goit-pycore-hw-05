import pytest
import inspect

from task_4 import task_4_main as main
from task_4.task_4_command_handlers import (
    add_contact,
    change_contact,
    show_phone,
    show_all,
    hello,
    exit_bot,
    help_command,
)
from task_4.task_4_custom_exceptions import InvalidCommand, ExitBot, NotFound

# ---------- FIXTURE ----------

@pytest.fixture
def contacts():
    return {}

# ---------- BASIC HANDLERS ----------

def test_hello():
    assert hello() == "How can I help you?"


def test_add_contact_success(contacts):
    result = add_contact(contacts, ["John", "12345"])
    assert result == "Contact added."
    assert contacts["John"] == "12345"


def test_add_contact_invalid_args(contacts):
    with pytest.raises(InvalidCommand):
        add_contact(contacts, ["OnlyName"])


def test_change_contact_success(contacts):
    add_contact(contacts, ["John", "11111"])
    result = change_contact(contacts, ["John", "99999"])
    assert result == "Contact updated."
    assert contacts["John"] == "99999"


def test_change_contact_not_found(contacts):
    with pytest.raises(NotFound) as e:
        change_contact(contacts, ["Alice", "123"])
    assert "Contact not found" in str(e.value)


def test_show_phone_success(contacts):
    add_contact(contacts, ["John", "12345"])
    assert show_phone(contacts, ["John"]) == "12345"


def test_show_phone_not_found(contacts):
    with pytest.raises(NotFound) as e:
        show_phone(contacts, ["Bob"])
    assert "Contact 'Bob' not found" in str(e.value)


def test_show_all_empty(contacts):
    with pytest.raises(NotFound) as e:
        show_all(contacts)
    assert "No contacts found" in str(e.value)


def test_show_all_multiple(contacts):
    add_contact(contacts, ["John", "12345"])
    add_contact(contacts, ["Alice", "67890"])
    result = show_all(contacts)
    assert "John: 12345" in result
    assert "Alice: 67890" in result


def test_help_command_success():
    commands = ["add: Add contact", "change: Change contact"]
    result = help_command(commands)
    assert "Available commands:" in result
    assert "add:" in result
    assert "change:" in result


def test_help_command_empty():
    with pytest.raises(NotFound) as e:
        help_command([])
    assert "No available commands found" in str(e.value)


def test_exit_bot_raises():
    with pytest.raises(ExitBot) as e:
        exit_bot()
    assert "Good bye!" in str(e.value)


# ---------- MAIN.PY: parse_input ----------

def test_parse_input_splits_command_and_args():
    command, args = main.parse_input("add John 12345")
    assert command == "add"
    assert args == ["John", "12345"]


def test_parse_input_no_args():
    command, args = main.parse_input("help")
    assert command == "help"
    assert args == []


# ---------- MAIN.PY: _get_command_description_list ----------

def test_get_command_description_list_contains_all():
    descriptions = main._get_command_description_list()
    assert any("add" in desc for desc in descriptions)
    assert any("hello" in desc for desc in descriptions)
    assert any("exit" in desc for desc in descriptions)


# ---------- MAIN.PY: _handle_user_input ----------

def test_handle_user_input_add_success():
    contacts = {}
    result = main._handle_user_input("add John 12345", contacts)
    assert result == "Contact added."
    assert contacts["John"] == "12345"


def test_handle_user_input_change_success():
    contacts = {"John": "123"}
    result = main._handle_user_input("change John 999", contacts)
    assert result == "Contact updated."
    assert contacts["John"] == "999"


def test_handle_user_input_phone_success():
    contacts = {"John": "555"}
    result = main._handle_user_input("phone John", contacts)
    assert result == "555"


def test_handle_user_input_show_all_success():
    contacts = {"John": "111", "Alice": "222"}
    result = main._handle_user_input("all", contacts)
    assert "John: 111" in result
    assert "Alice: 222" in result


def test_handle_user_input_help_success():
    result = main._handle_user_input("help", {})
    assert "Available commands:" in result
    assert "add:" in result


def test_handle_user_input_invalid_command():
    with pytest.raises(InvalidCommand):
        main._handle_user_input("unknowncmd", {})


def test_handle_user_input_invalid_args_add():
    with pytest.raises(InvalidCommand):
        main._handle_user_input("add John", {})


def test_handle_user_input_not_found_contact():
    with pytest.raises(NotFound):
        main._handle_user_input("phone Roman", {})


def test_handle_user_input_exit_command():
    with pytest.raises(ExitBot):
        main._handle_user_input("exit", {})


# ---------- MAIN.PY: inspect fallback ----------

def test_inspect_signature_matches_handler_params():
    for cmd, meta in main.COMMANDS.items():
        handler = meta["handler"]
        sig = inspect.signature(handler)

        assert hasattr(sig.parameters, "keys")
        assert len(sig.parameters) <= 2
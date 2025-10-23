import pytest
from task_3.task_3 import (
    parse_log_line,
    load_logs,
    filter_logs_by_level,
    count_logs_by_level,
)


# ---------- FIXTURES ----------

@pytest.fixture
def sample_log_lines():
    return [
        "2024-01-22 08:30:01 INFO User logged in successfully.",
        "2024-01-22 08:45:23 DEBUG Attempting to connect to the database.",
        "2024-01-22 09:00:45 ERROR Database connection failed.",
        "2024-01-22 09:15:10 INFO Data export completed.",
        "2024-01-22 10:30:55 WARNING Disk usage above 80%.",
    ]


@pytest.fixture
def tmp_log_file(tmp_path, sample_log_lines):
    log_file = tmp_path / "test_log.log"
    log_file.write_text("\n".join(sample_log_lines), encoding="utf-8")
    return log_file


# ---------- parse_log_line ----------

def test_parse_log_line_valid(sample_log_lines):
    line = sample_log_lines[0]
    result = parse_log_line(line)
    assert result["date"] == "2024-01-22"
    assert result["time"] == "08:30:01"
    assert result["level"] == "INFO"
    assert "User logged in" in result["message"]


def test_parse_log_line_incorrect_format():
    bad_line = "This line is invalid"
    with pytest.raises(ValueError) as e:
        parse_log_line(bad_line)
    assert "Incorrect log format" in str(e.value)


def test_parse_log_line_lowercase_level():
    line = "2024-01-22 10:00:00 info lowercase test"
    result = parse_log_line(line)
    assert result["level"] == "INFO"


# ---------- load_logs ----------

def test_load_logs_success(tmp_log_file):
    logs = load_logs(tmp_log_file)
    assert isinstance(logs, list)
    assert len(logs) == 5
    assert all("level" in log for log in logs)


def test_load_logs_file_not_found():
    with pytest.raises(FileNotFoundError) as e:
        load_logs("nonexistent.log")
    assert "not found" in str(e.value)


def test_load_logs_with_bad_line(tmp_path):
    bad_file = tmp_path / "bad_log.log"
    bad_file.write_text("2024-01-22 WRONG LINE FORMAT", encoding="utf-8")
    with pytest.raises(ValueError):
        load_logs(bad_file)


# ---------- filter_logs_by_level ----------

def test_filter_logs_by_level_returns_correct_subset(sample_log_lines):
    logs = [parse_log_line(line) for line in sample_log_lines]
    filtered = filter_logs_by_level(logs, "ERROR")
    assert len(filtered) == 1
    assert filtered[0]["level"] == "ERROR"
    assert "Database connection failed" in filtered[0]["message"]


def test_filter_logs_by_level_case_insensitive(sample_log_lines):
    logs = [parse_log_line(line) for line in sample_log_lines]
    filtered = filter_logs_by_level(logs, "warning")
    assert len(filtered) == 1
    assert filtered[0]["level"] == "WARNING"


def test_filter_logs_by_level_empty(sample_log_lines):
    logs = [parse_log_line(line) for line in sample_log_lines]
    filtered = filter_logs_by_level(logs, "CRITICAL")
    assert filtered == []


# ---------- count_logs_by_level ----------

def test_count_logs_by_level_counts_correctly(sample_log_lines):
    logs = [parse_log_line(line) for line in sample_log_lines]
    result = count_logs_by_level(logs)
    assert result["INFO"] == 2
    assert result["DEBUG"] == 1
    assert result["ERROR"] == 1
    assert result["WARNING"] == 1


def test_count_logs_by_level_empty_list():
    assert count_logs_by_level([]) == {}


def test_count_logs_by_level_multiple_entries(sample_log_lines):
    lines = sample_log_lines + [
        "2024-01-22 14:00:00 ERROR Second error message."
    ]
    logs = [parse_log_line(line) for line in lines]
    counts = count_logs_by_level(logs)
    assert counts["ERROR"] == 2

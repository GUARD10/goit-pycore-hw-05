import sys
from typing import List, Dict

import re

def parse_log_line(line: str) -> dict:
    pattern = r"^(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)$"
    match = re.match(pattern, line.strip())
    if not match:
        raise ValueError(f"Incorrect log format: {line.strip()}")
    date, time, level, message = match.groups()
    return {"date": date, "time": time, "level": level.upper(), "message": message}


def load_logs(file_path: str) -> List[dict]:
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    logs.append(parse_log_line(line))
    except FileNotFoundError:
        raise FileNotFoundError(f"Failed: file '{file_path}' not found.")
    except ValueError:
        raise
    except Exception as e:
        raise Exception(f"Error while reading file: {e}")
    return logs


def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    return list(filter(lambda log: log["level"] == level.upper(), logs))


def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: Dict[str, int]) -> None:
    print("\nLog level | Count")
    print("----------|------")
    for level, count in counts.items():
        print(f"{level:<9} | {count}")


def display_logs_by_level(logs: List[dict], level: str) -> None:
    print(f"\nLog details for '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


def main():
    try:
        file_path = sys.argv[1]
    except IndexError:
        print("Use: python task_3.py <log_file_path> [<log_level>]")
        sys.exit(1)

    level = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        logs = load_logs(file_path)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

        if level:
            filtered = filter_logs_by_level(logs, level)
            if filtered:
                display_logs_by_level(filtered, level)
            else:
                print(f"\nLevel '{level}' not found in logs.")
    except Exception as ex:
        print(f"Error: {ex}")
        sys.exit(1)


if __name__ == "__main__":
    main()

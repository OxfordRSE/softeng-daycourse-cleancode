# Extended exercise: Refactor the following (long) function into smaller, more
# manageable functions, while maintaining the same functionality (i.e. tests must pass).
#
# ------------------------------------------------------------------
# Task                           | Suggested Function Name
# ------------------------------------------------------------------
# Load and parse JSON            | load_user_data(filepath)
# Filter and enrich active users | filter_active_users(data)
# Compute age statistics         | compute_age_stats(users)
# Group users by country         | group_users_by_country(users)
# Generate report string         | format_report(stats, groups)
# Log the report to file         | log_report(report, path="...")
# ------------------------------------------------------------------

import os
import json
import statistics
from datetime import datetime


def process_user_data(filepath):
    """
    Load user data from a JSON file, filter active users, calculate age stats,
    group by country, format a report, and log to a file.
    """
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    active_users = []
    for user in data:
        if user.get("is_active") and user.get("birthdate") and user.get("country"):
            try:
                birthdate = datetime.strptime(user["birthdate"], "%Y-%m-%d")
                age = (datetime.now() - birthdate).days // 365
                user["age"] = age
                active_users.append(user)
            except ValueError:
                continue

    ages = [u["age"] for u in active_users]
    average_age = statistics.mean(ages) if ages else None
    median_age = statistics.median(ages) if ages else None
    max_age = max(ages) if ages else None
    min_age = min(ages) if ages else None

    countries = {}
    for user in active_users:
        country = user["country"]
        if country not in countries:
            countries[country] = []
        countries[country].append(user)

    report_lines = []
    report_lines.append(f"Processed {len(data)} users, {len(active_users)} active")
    report_lines.append("Age statistics:")
    report_lines.append(f"  Average: {average_age}")
    report_lines.append(f"  Median: {median_age}")
    report_lines.append(f"  Max: {max_age}")
    report_lines.append(f"  Min: {min_age}")
    report_lines.append("User distribution by country:")
    for country, users in countries.items():
        report_lines.append(f"  {country}: {len(users)} users")

    report = "\n".join(report_lines)
    print(report)

    try:
        with open("user_report.log", "a") as log_file:
            log_file.write(f"\n[{datetime.now().isoformat()}]\n{report}\n")
    except Exception as e:
        print(f"Error writing log: {e}")


def test_process_user_data(tmp_path, capsys):
    # Create test JSON data
    users = [
        {"name": "Alice", "is_active": True, "birthdate": "1990-01-01", "country": "USA"},
        {"name": "Bob", "is_active": True, "birthdate": "1985-05-20", "country": "Canada"},
        {"name": "Charlie", "is_active": False, "birthdate": "1992-03-15", "country": "UK"},
        {"name": "Dana", "is_active": True, "birthdate": "not-a-date", "country": "Germany"},
        {"name": "Eve", "is_active": True, "birthdate": "2001-09-09", "country": "USA"}
    ]

    # Write test data to temporary JSON file
    test_file = tmp_path / "test_users.json"
    with open(test_file, "w") as f:
        json.dump(users, f)

    # Change working directory to tmp_path so log file is written there
    old_cwd = os.getcwd()
    os.chdir(tmp_path)

    try:
        # Run the function
        process_user_data(test_file)

        # Capture stdout
        output = capsys.readouterr().out

        # Assertions
        assert "Processed 5 users, 3 active" in output
        assert "Average:" in output
        assert "USA: 2 users" in output
        assert "Canada: 1 users" in output

        # Check the log file
        log_file = tmp_path / "user_report.log"
        assert log_file.exists()
        with open(log_file) as f:
            log = f.read()
            assert "Processed 5 users, 3 active" in log
            assert "USA: 2 users" in log

    finally:
        os.chdir(old_cwd)

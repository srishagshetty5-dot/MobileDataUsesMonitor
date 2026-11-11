# Mobile Data Usage Monitor

**Python Programming - Activity 2: User-Defined Package Development**

| | |
|---|---|
| **Name** | Srisha G Shetty |
| **USN** | 25BCAR0427 |
| **Name** | Shreesha U |
| **USN** | 25BCAR0174  |
| **Course** | BCA |
| **Department** | CS & IT |
| **Submitted to** | Dr. Ramkumar Krishnamurthi |

## Problem Statement

Mobile users often use up their data quota before the billing cycle ends without noticing.
This project tracks daily data usage, shows how much data is left and estimates the day
on which the quota will run out.

## Features

- Record daily data usage (repeated entries for the same day are added together)
- Calculate remaining data from the quota
- Calculate average daily usage
- Estimate the day the quota will run out
- Input validation for invalid and boundary cases

## Project Structure

```
ProjectFolder/
├── datausage_pkg/
│   ├── __init__.py      # exposes the package functions
│   └── ActualTask.py    # function definitions
├── main.py              # main program (outside the package folder)
├── sample_output.txt    # captured output
└── README.md
```

## How to Run

1. Keep `main.py` and the `datausage_pkg` folder together in the same folder.
2. Open a terminal in that folder (the one containing `main.py`).
3. Run:

```
python main.py
```

Requires Python 3. No external libraries are needed.

## Functions (`datausage_pkg/ActualTask.py`)

| Function | Description |
|---|---|
| `record_usage(usage_log, day, mb_used)` | Stores the MB used on a day of the billing cycle |
| `remaining_data(quota_gb, usage_log)` | Returns the remaining data in MB (never below 0) |
| `daily_average(usage_log)` | Returns the average MB used per recorded day |
| `estimate_exhaustion(quota_gb, usage_log)` | Returns the day number on which the data will run out |

Usage is recorded in MB, the quota is given in GB, and 1 GB = 1024 MB.

## Input Validation

| Invalid input | Result |
|---|---|
| Negative data usage | `ValueError` |
| Day outside 1-31 | `ValueError` |
| Quota is zero or negative | `ValueError` |
| Average requested with no records | `ValueError` |

## Test Cases

| # | Scenario | Result |
|---|---|---|
| 1 | Normal usage over 5 days | 936 MB left, runs out on day 13 |
| 2 | Same day recorded twice | Usage added to 500 MB |
| 3 | Edge: usage equals the quota | Remaining 0 MB |
| 4 | Edge: usage exceeds the quota | Remaining 0 MB (not negative) |
| 5 | Edge: zero usage | Data never runs out |
| 6 | Invalid inputs | All 4 cases are caught with clear messages |

## Sample Output

```
--- Test 1: Normal usage ---
Usage log (day: MB): {1: 120, 2: 90, 3: 150, 4: 110, 5: 130}
Quota: 1.5 GB
Remaining data: 936.0 MB
Average daily usage: 120.0 MB
Data will run out on day 13

--- Test 6: Invalid inputs ---
Negative usage: Data used cannot be negative
Day 32: Day must be between 1 and 31
Zero quota: Quota must be greater than zero
Empty log: No usage recorded yet
```

The full output is in `sample_output.txt`.

## Note

All data used in this project is sample (simulated) data. No real personal information is included.

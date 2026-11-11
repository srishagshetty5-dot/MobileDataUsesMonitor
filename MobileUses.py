
from MobileDataUses_pkg import record_usage, remaining_data, daily_average, estimate_exhaustion

QUOTA_GB = 1.5   # total data quota (in GB)


def show_summary(title, usage_log):
    print("\n--- " + title + " ---")
    print("Usage log (day: MB):", usage_log)
    print("Quota:", QUOTA_GB, "GB")
    print("Remaining data:", round(remaining_data(QUOTA_GB, usage_log), 2), "MB")
    print("Average daily usage:", round(daily_average(usage_log), 2), "MB")

    day = estimate_exhaustion(QUOTA_GB, usage_log)
    if day is None:
        print("Data will not run out (usage is 0)")
    else:
        print("Data will run out on day", day)


# Test 1: Normal case
log1 = {}
record_usage(log1, 1, 120)
record_usage(log1, 2, 90)
record_usage(log1, 3, 150)
record_usage(log1, 4, 110)
record_usage(log1, 5, 130)
show_summary("Test 1: Normal usage", log1)

# Test 2: Same day recorded twice
log2 = {}
record_usage(log2, 1, 200)
record_usage(log2, 1, 300)
show_summary("Test 2: Same day recorded twice", log2)

# Test 3: Edge case - usage exactly equals the quota
log3 = {}
record_usage(log3, 1, 1024)
record_usage(log3, 2, 512)
show_summary("Test 3 (Edge): Usage equals quota", log3)

# Test 4: Edge case - usage more than the quota
log4 = {}
record_usage(log4, 1, 1000)
record_usage(log4, 2, 900)
show_summary("Test 4 (Edge): Usage exceeds quota", log4)

# Test 5: Edge case - zero usage
log5 = {}
record_usage(log5, 1, 0)
record_usage(log5, 2, 0)
show_summary("Test 5 (Edge): Zero usage", log5)

# Test 6: Invalid inputs
print("\n--- Test 6: Invalid inputs ---")

try:
    record_usage({}, 3, -50)
except ValueError as error:
    print("Negative usage:", error)

try:
    record_usage({}, 32, 100)
except ValueError as error:
    print("Day 32:", error)

try:
    remaining_data(0, {1: 100})
except ValueError as error:
    print("Zero quota:", error)

try:
    daily_average({})
except ValueError as error:
    print("Empty log:", error)
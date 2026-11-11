
def record_usage(usage_log, day, mb_used):
    """Save the data used on a day."""
    if day < 1 or day > 31:
        raise ValueError("Day must be between 1 and 31")
    if mb_used < 0:
        raise ValueError("Data used cannot be negative")

    if day in usage_log:
        usage_log[day] = usage_log[day] + mb_used   # same day again, so add it
    else:
        usage_log[day] = mb_used
    return usage_log


def remaining_data(quota_gb, usage_log):
    """Return the remaining data in MB."""
    if quota_gb <= 0:
        raise ValueError("Quota must be greater than zero")

    total_used = 0
    for mb in usage_log.values():
        total_used = total_used + mb

    remaining = quota_gb * 1024 - total_used
    if remaining < 0:
        remaining = 0
    return remaining


def daily_average(usage_log):
    """Return the average MB used per recorded day."""
    if len(usage_log) == 0:
        raise ValueError("No usage recorded yet")

    total = sum(usage_log.values())
    return total / len(usage_log)


def estimate_exhaustion(quota_gb, usage_log):
    """Return the day number when the data will run out."""
    left = remaining_data(quota_gb, usage_log)
    average = daily_average(usage_log)
    day = max(usage_log.keys())         

    if left == 0:
        return day                    
    if average == 0:
        return None                      

    while left > 0:
        day = day + 1
        left = left - average
    return day

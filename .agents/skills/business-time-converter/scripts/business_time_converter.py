import argparse
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


def add_business_days(start_date, days):
    current = start_date
    step = 1 if days >= 0 else -1
    remaining = abs(days)

    while remaining > 0:
        current += timedelta(days=step)
        if current.weekday() < 5:
            remaining -= 1

    return current


def generate_recurrences(start_dt, frequency, count):
    dates = []

    for i in range(count):
        if frequency == "daily":
            dates.append(start_dt + timedelta(days=i))
        elif frequency == "weekly":
            dates.append(start_dt + timedelta(weeks=i))
        elif frequency == "monthly":
            month = start_dt.month - 1 + i
            year = start_dt.year + month // 12
            month = month % 12 + 1
            day = min(start_dt.day, 28)
            dates.append(start_dt.replace(year=year, month=month, day=day))
        else:
            raise ValueError("Frequency must be daily, weekly, or monthly.")

    return dates


def main():
    parser = argparse.ArgumentParser(description="Business time planner")

    parser.add_argument("--start", required=True,
                        help="Start datetime, e.g. 2026-05-01 09:00")
    parser.add_argument("--source-tz", required=True,
                        help="Source timezone, e.g. America/New_York")
    parser.add_argument("--target-tz", nargs="+",
                        required=True, help="Target time zones")
    parser.add_argument("--business-days", type=int,
                        default=0, help="Business day offset")
    parser.add_argument(
        "--frequency", choices=["daily", "weekly", "monthly"], default=None)
    parser.add_argument("--count", type=int, default=1)

    args = parser.parse_args()

    start_dt = datetime.strptime(args.start, "%Y-%m-%d %H:%M")
    start_dt = start_dt.replace(tzinfo=ZoneInfo(args.source_tz))

    if args.business_days != 0:
        shifted_date = add_business_days(start_dt.date(), args.business_days)
        start_dt = datetime.combine(
            shifted_date,
            start_dt.time(),
            tzinfo=ZoneInfo(args.source_tz)
        )

    if args.frequency:
        occurrences = generate_recurrences(
            start_dt, args.frequency, args.count)
    else:
        occurrences = [start_dt]

    print("| # | Source Time | " + " | ".join(args.target_tz) + " |")
    print("|---|---|" + "|".join(["---"] * len(args.target_tz)) + "|")

    for idx, occurrence in enumerate(occurrences, start=1):
        converted_times = [
            occurrence.astimezone(ZoneInfo(tz)).strftime("%Y-%m-%d %H:%M %Z")
            for tz in args.target_tz
        ]

        print(
            f"| {idx} | {occurrence.strftime('%Y-%m-%d %H:%M %Z')} | "
            + " | ".join(converted_times)
            + " |"
        )


if __name__ == "__main__":
    main()

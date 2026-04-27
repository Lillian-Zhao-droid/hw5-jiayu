---
name: business-time-converter
description: Calculate workday offsets, time zone conversions, and simple recurring schedules. This feature is particularly useful for planning meetings or deadlines, allowing users to calculate dates, convert times across time zones, skip weekends, or generate recurring calendar dates.
---

# Business Time converter Skill

## When to use this skill

Use this skill when the user needs deterministic date/time calculations, including:

- converting a time between time zones
- adding or subtracting business days
- generating repeated meeting or deadline dates
- checking dates while skipping weekends

## When not to use this skill

Do not use this skill for:

- legal, payroll, or compliance deadlines that require official holiday calendars
- vague scheduling advice without a concrete date or time
- personal calendar booking or sending invitations
- complex recurrence rules beyond daily, weekly, or monthly patterns

## Expected inputs

The user should provide:

- a start date or date + time
- the source time zone
- one or more target time zones
- optional business-day offset
- optional recurrence frequency
- optional number of occurrences

## Deterministic script role

The Python script performs the exact date and time calculations. This is necessary because language models can make mistakes with:

- daylight saving time
- weekday counting
- time-zone offsets
- repeated date generation

The assistant should explain the result, but the script must compute the actual dates and times.

## Step-by-step instructions

1. Identify the user's start date and time.
2. Identify the source time zone.
3. Identify the requested target time zones.
4. Determine whether the user needs:
   - time-zone conversion
   - business-day offset
   - recurrence generation
5. Run the Python script with the correct arguments.
6. Present the results in a clear table.
7. Mention limitations, especially that holidays are not included unless explicitly added.

## Expected output format

Return:

- a short summary
- a table with dates and converted times
- any warnings or assumptions

## Limitations

This skill skips weekends when calculating business days, but it cannot automatically recognize company holidays or public holidays in specific countries, so the results are often not directly applicable in practice. However, the time zone conversion feature is very effective; its limitation is that it cannot be directly linked to meeting software for scheduling purposes.

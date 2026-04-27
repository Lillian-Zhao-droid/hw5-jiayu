# HW5 - Business Time Converter Skill

## Overview

This project creates a reusable AI skill called **business-time-converter**.

The skill helps users perform deterministic date and time calculations that language models may not handle reliably on their own.

It supports:

- business-day offsets (skip weekends)
- time-zone conversions
- recurring schedules
- meeting and deadline planning across regions

---

## What the Skill Does

This skill converts dates and times between time zones, adds or subtracts business days, and generates simple recurring schedules.

Examples:

- Convert 9:00 AM New York time to London and Shanghai time
- Add 3 business days to a Friday while skipping the weekend
- Generate a weekly recurring meeting schedule for 4 weeks

---

## Why I chose this skill

I chose this topic because I frequently need to hold online meetings with people living in China or the UK. Since large language models (LLMs) are not yet very accurate in this area, manual verification is often required. While language models can easily explain how dates and times are calculated, performing these calculations reliably is difficult. If we rely solely on natural language processing, factors such as time zones, daylight saving time, days of the week, and recurrence rules can all lead to errors.

## How to Use It

Example command:

```bash
python .agents/skills/business-time-converter/scripts/business_time_converter.py \
--start "2026-05-01 09:00" \
--source-tz America/New_York \
--target-tz Europe/London Asia/Shanghai \
--frequency weekly \
--count 4

---

## What the Script Does

The Python script performs the deterministic part of the workflow.

Main functions include:

add_business_days()
Adds or subtracts weekdays
Automatically skips Saturday and Sunday
generate_recurrences()

Creates recurring schedules using:
--daily
--weekly
--monthly
main()
--Reads user arguments
--Applies business-day logic
--Converts time zones
--Generates recurrence schedules
--Returns results in table format

---

## What Worked Well

This skill worked well because:

--The AI agent successfully discovered the skill using the SKILL.md name and description
--The agent knew when to activate the skill for date/time requests
--The Python script handled exact calculations more reliably than manual reasoning
--Final outputs were clear, structured, and reusabl

---

## Limitations Remaining

Current limitations include:

--weekends are skipped, but public holidays in some specific countries or regions are not included
--monthly recurrence uses simplified logic
--legal or compliance deadlines should not rely only on this tool
--does not connect directly to Google Calendar or Outlook

## Demo Video Link
```

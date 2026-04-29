import csv

room_counts = {}
type_counts = {}
day_attendees = {}
all_events = []

with open("bookings.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        room = row["room"].strip()
        event_type = row["event_type"].strip()
        date = row["date"].strip()
        attendees = int(row["attendees"])

        room_counts[room] = room_counts.get(room, 0) + 1
        type_counts[event_type] = type_counts.get(event_type, 0) + 1
        day_attendees[date] = day_attendees.get(date, 0) + attendees

        row["attendees"] = attendees
        all_events.append(row)

busiest_day = max(day_attendees, key=day_attendees.get)
busiest_count = day_attendees[busiest_day]

large_events = [event for event in all_events if event["attendees"] > 50]
large_events_sorted = sorted(
    large_events,
    key=lambda event: event["attendees"],
    reverse=True
)

print("=== Community Centre Booking Report ===")

print("\nBookings by Room:")
for room in sorted(room_counts):
    print(f"  {room:<6}: {room_counts[room]} events")

print("\nBookings by Event Type:")
for etype in sorted(type_counts):
    print(f"  {etype:<8}: {type_counts[etype]} events")

print(f"\nBusiest Day: {busiest_day}  ({busiest_count} total attendees)")

print("\nLarge Events (> 50 attendees):")
for event in large_events_sorted:
    print(
        f"  {event['date']} | "
        f"{event['room']:<7} | "
        f"{event['event_type']:<8} | "
        f"{event['attendees']:>3} attendees"
    )
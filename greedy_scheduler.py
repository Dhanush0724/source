def greedy_scheduler(jobs, time_slots):
    schedule = {}
    for job in jobs:
        # Sort available time slots by their starting time
        available_slots = sorted(time_slots, key=lambda slot: slot[0])
        for slot in available_slots:
            if slot[1] >= job[1]:  # Check if the job can fit in the time slot
                schedule[job[0]] = slot
                time_slots.remove(slot)  # Remove the slot from available slots
                break
    return schedule 
    

# Define jobs as (job_name, job_duration)
jobs = [("Job1", 4), ("Job2", 2), ("Job3", 4)]

# Define time slots as (start_time, end_time)
time_slots = [(1, 3), (4, 7), (7, 10), (10, 12)]

# Use the greedy scheduler to create a schedule
schedule = greedy_scheduler(jobs, time_slots)
print(schedule)

# Print the schedule
for job, slot in schedule.items():
    print(f"{job} is scheduled from {slot[0]} to {slot[1]}")

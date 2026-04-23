def job_sequencing():
    n = int(input("Enter number of jobs: "))
    jobs = []

    # Input jobs
    for i in range(n):
        job_id = input("Enter job id: ")
        deadline = int(input("Enter deadline: "))
        profit = int(input("Enter profit: "))
        jobs.append((job_id, deadline, profit))

    # Sort jobs by profit (descending)
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [-1] * max_deadline

    total_profit = 0

    # Assign jobs
    for job in jobs:
        job_id, deadline, profit = job

        for i in range(deadline - 1, -1, -1):
            if slots[i] == -1:
                slots[i] = job_id
                total_profit += profit
                break

    # Output
    print("Selected Jobs:", [j for j in slots if j != -1])
    print("Total Profit:", total_profit)


job_sequencing()
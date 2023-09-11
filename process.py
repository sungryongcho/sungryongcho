def solution(priorities, location):
    answer = 0
    printer = [(i, p) for i, p in enumerate(priorities)]

    while printer:
        job = printer.pop(0)
        if any(job[1] < other_job[1] for other_job in printer):
            printer.append(job)
        else:
            answer = answer + 1
            if job[0] == location:
                break

    return answer
"""Number of Students Doing HW at a Given Time

Provided parameters:
    (1) `start_time` -- integer array
    (2) `end_time` -- integer array
    (3) `query_time` -- integer

The `ith` student started their HW at time `start_time[i]` and finished it at the time `end_time[i]`.

Return the NUMBER OF STUDENTS doing their hw at time `query_time`. More formally, return the number of students where `query_time` lays in the interval (start_time[i], end_time[i]) inclusive.
"""

from queue import Queue

def students_doing_work(start_time, end_time, query_time):
    number_of_students = 0
    for i in range(len(end_time)):
        if start_time[i] <= query_time and end_time[i] >= query_time:
            number_of_students += 1
    return number_of_students

if __name__ == "__main__":
    print(students_doing_work([1, 2, 2], [2, 3, 5], 4))
    print(students_doing_work([1, 2, 2], [2, 3, 5], 2))
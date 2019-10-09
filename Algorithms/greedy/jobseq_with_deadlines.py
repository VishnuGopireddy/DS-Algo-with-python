'''
Given an array of jobs where every job has a deadline and associated profit if the job is finished before the deadline.
It is also given that every job takes single unit of time, so the minimum possible deadline for any job is 1.
How to maximize total profit if only one job can be scheduled at a time.
'''

def jobseq(arr):
    chart = [0 for i in range(4)]
    jobs = {i[2]:[i[0],i[1]] for i in arr}
    jobs = sorted(jobs.items(),reverse=True)



arr = [['a', 2, 100], # Job Array
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]


jobseq(arr)

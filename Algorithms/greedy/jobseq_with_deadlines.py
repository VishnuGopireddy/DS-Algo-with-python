'''
https://www.geeksforgeeks.org/job-sequencing-problem/
Given an array of jobs where every job has a deadline and associated profit if the job is finished before the deadline.
It is also given that every job takes single unit of time, so the minimum possible deadline for any job is 1.
How to maximize total profit if only one job can be scheduled at a time.
TIME Complexity => O(nlogn) + O (n)
'''


def jobseq(arr):
    jobs = {i[2]:[i[0],i[1]] for i in arr}
    jobs = dict(sorted(jobs.items(),reverse=True))
    print(jobs)
    chart = [0 for i in range(len(jobs))]
    profit = 0
    for i in jobs:
        print(i)
        j = jobs[i][1]
        while j > 0:
            if chart[j] == 0:
                chart[j] = jobs[i][0]
                profit = profit + i
                break
            j = j - 1
    print(chart[1:],profit)


arr = [['a', 2, 100], # Job Array
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]

jobseq(arr)

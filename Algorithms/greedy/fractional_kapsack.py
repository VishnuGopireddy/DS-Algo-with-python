'''
Given weights and values of n items, we need to put these items in a knapsack of capacity W to
get the maximum total value in the knapsack.

In Fractional Knapsack, we can break items for maximizing the total value of knapsack.
This problem in which we can break an item is also called the fractional knapsack problem.

Input:
  Items as (value, weight) pairs
  arr[] = {{60, 10}, {100, 20}, {120, 30}}
  Knapsack Capacity, W = 50;
Time Complexity: O(nlogn) + O(n)
'''

def fractioanl_knapsack(values, weights,capacity):
    '''
    :param items: two lists values and weight:
    :return: Total value of profits .
    '''
    #take p/e dictionay
    profit_weight = {i/j:[i,j] for i,j in zip(values,weights)}
    #Sort p/e dict in reverse order
    profit_weight = dict(sorted(profit_weight.items(),reverse=True))
    #Fill knapsack
    tot_value = 0
    for i in profit_weight:
        if capacity - profit_weight[i][1] > 0:
            capacity = capacity - profit_weight[i][1]
            tot_value = tot_value + profit_weight[i][0]
        else:
            fraction = capacity / profit_weight[i][1]
            tot_value = tot_value + (profit_weight[i][0] * fraction)
            capacity = capacity - (profit_weight[i][1] * fraction)
    print(tot_value)

wt = [10, 40, 20, 30]
val = [60, 40, 100, 120]
capacity = 50
fractioanl_knapsack(val, wt, capacity)
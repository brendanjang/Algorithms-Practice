graph = dict()
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}

infinity = float('inf')
costs = dict()
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = dict()
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    # go through each node
    for node in costs:
        cost = costs[node]
        # if its the lowest cost so far and has not been processed
        if cost < lowest_cost and node not in processed:
            # set as new lowest-cost node
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# find lowest cost node that hasn't been processed
node = find_lowest_cost_node(costs)

# loop finishes when processed all nodes
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    # go through neighbors of node
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # if its cheaper to get to neighbor by going through this node
        if costs[n] > new_cost:
            # update costs for node
            costs[n] = new_cost
            # node becomes the new parent for this neighbor
            parents[n] = node
    # mark node as processed
    processed.append(node)
    # find next node and loop
    node = find_lowest_cost_node(costs)

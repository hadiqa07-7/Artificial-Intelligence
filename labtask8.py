#-------------GFBS---------------------------------
import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    open_list = [(heuristic[start], start, [start])]  # (priority, node, path)
    visited = set()

    while open_list:
        _, node, path = heapq.heappop(open_list) # will return the one with the minimum value as its min heap

        if node == goal:
            return path   # ✅ return path instead of just True

        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(open_list, (heuristic[neighbor], neighbor, path + [neighbor]))

    return None  # if no path found

graph = {
    'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
    'Sibiu': ['Fagaras', 'Rimnicu'],
    'Timisoara': ['Lugoj'],
    'Zerind': ['Oradea'],
    'Fagaras': ['Bucharest'],
    'Rimnicu': ['Pitesti'],
    'Pitesti': ['Bucharest'],
    'Bucharest': []
}

heuristic = {
    'Arad': 366, 'Sibiu': 253, 'Timisoara': 329, 'Zerind': 374,
    'Fagaras': 176, 'Rimnicu': 193, 'Pitesti': 100, 'Bucharest': 0
}

path = greedy_best_first_search(graph, 'Arad', 'Bucharest', heuristic)
print("Path:", path)




#-------------------------------A*---------------------------------------------------------------
import heapq

def a_star_search(graph, start, goal, heuristic):
    # OPEN list as a priority queue (f, g, node, path)
    open_list = [(heuristic[start],0, start, [start])]
    visited = {}  # stores best g cost for each node 0

    while open_list:
        f, g, node, path = heapq.heappop(open_list) #min based on f value

        # Goal check
        if node == goal:
            return path, g   # return path and cost

        # If we already found a cheaper way, skip
        if node in visited and visited[node] <= g:  #means that if we already have the cheapest path for that node and its being visited 
            #again and this time it costs more so skip this path we dont need it we already have the cheapest one so far for this node 
         continue #we start from while loop again
        visited[node] = g #other option if g is lesser this time then we add it to visited with this val and expland its neigbors

        # Expand neighbors
        for neighbor, cost in graph.get(node, []):
            new_g = g + cost
            new_f = new_g + heuristic[neighbor]
            heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')  # No path found

graph = {
    'Arad': [('Sibiu', 140), ('Timisoara', 118), ('Zerind', 75)],
    'Sibiu': [('Fagaras', 99), ('Rimnicu', 80)],
    'Timisoara': [('Lugoj', 111)],
    'Zerind': [('Oradea', 71)],
    'Fagaras': [('Bucharest', 211)],
    'Rimnicu': [('Pitesti', 97)],
    'Pitesti': [('Bucharest', 101)],
    'Bucharest': []
}

heuristic = {
    'Arad': 366, 'Sibiu': 253, 'Timisoara': 329, 'Zerind': 374,
    'Fagaras': 176, 'Rimnicu': 193, 'Pitesti': 100, 'Bucharest': 0
}

path, cost = a_star_search(graph, 'Arad', 'Bucharest', heuristic)
print("Optimal Path:", path)
print("Total Cost:", cost)
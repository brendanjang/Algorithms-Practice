from collections import deque


# function to tell if person is a match
def match(name):
    return name[-1] == 'm'


def bfs(name):
    # create new queue
    search_queue = deque()
    # add all neighbors to search queue
    search_queue += graph['you']
    # list to keep track of already searched people
    searched = []
    while search_queue:
        # take first person off queue
        person = search_queue.popleft()
        # check if match
        if match(person):
            print(person + ' is a match!')
            return True
        else:
            # if not match, add the person's neighbors to search queue
            search_queue += graph[person]
            # mark person as searched
            searched.append(person)
    # nobody in this queue was a match
    return False


# create dict and map nodes to all of its neighbors
graph = dict()
graph['you'] = ['alice', 'bob', 'claire']
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

bfs('you')





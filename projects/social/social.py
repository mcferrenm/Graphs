import random


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {
            8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
        # !!!! IMPLEMENT ME

        # Add users
        # Time Complexity: O(numUsers)
        # Space Complexity: O(numUsers)
        # for i in range(numUsers):
        #     self.addUser(f"User {i + 1}")

        # # Create friendships
        # possibleFriendships = []
        # for userID in self.users:
        #     for friendID in range(userID + 1, self.lastID + 1):
        #         possibleFriendships.append((userID, friendID))

        # # Time Complexity: O(numUsers ^ 2)
        # # Space Complexity: O(1)
        # random.shuffle(possibleFriendships)

        # # Time Complexity: O(avgFriendships * numUsers // 2)
        # # Space Complexity: O(avgFriendships * numUsers // 2)
        # for friendship_index in range(avgFriendships * numUsers // 2):
        #     # print(friendship_index)
        #     friendship = possibleFriendships[friendship_index]
        #     self.addFriendship(friendship[0], friendship[1])
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty Queue
        q = Queue()
        # Create an empty Visited set
        visited = set()
        # Add A PATH TO the starting vertex to the queue
        q.enqueue([starting_vertex])
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex of the path
            v = path[-1]
            # Check if it's our destination
            if v == destination_vertex:
                return path
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited (add it to the visited set)
                visited.add(v)
                # Then enqueue PATHS TO each of its neighbors in the queue
                for neighbor in self.friendships[v]:
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}

        # for friend in self.friendships[userID]:
        #     visited[userID] = [userID]
        #     visited[friend] = self.bfs(userID, friend)
        #     # print(friend)
        #     # if friend not in visited:
        #     # 

            # Create an empty Queue
        q = Queue()
        # Create an empty Visited set
        visited = {}
        # Add A PATH TO the starting vertex to the queue
        q.enqueue([userID])
        # While the queue is not empty...
        while q.size() > 0:
            # print(q.queue)
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex of the path
            v = path[-1]
            # Check if it's our destination
            # if v == destination_vertex:
            #     return path
            # If it has not been visited...
            if v not in visited:
                visited[v] = path
                # Then enqueue PATHS TO each of its neighbors in the queue
                for friend in self.friendships[v]:
                    if friend not in visited:
                        path_copy = path.copy()
                        path_copy.append(friend)
                        q.enqueue(path)  

                    # for other_f in self.friendships[friend]:
                    #     # print(friend, other_f)
                    #     # friend = 10
                    #     if other_f not in visited:
                    #         path_copy = path.copy()
                    #         path_copy.append(other_f)
            # else:


        #         # for friend in self.friendships[userID]:
        #         #     visited[friend] = self.bfs(userID, friend)

        print(visited)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    # print(connections)

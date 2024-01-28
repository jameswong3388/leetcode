class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        # Create an adjacency list to store the edges of the graph
        adj_list = [[] for i in range(n)]  # [[], [], [], [], [], []]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        # adj_list = [[1, 2], [0], [0], [5, 4], [5, 3], [3, 4]]

        # Mark all vertices as not visited
        visited = [False] * n  # [False, False, False, False, False, False]

        # Recursive function to check if there is a path from source to destination
        def dfs(vertex):
            # Mark the current vertex as visited
            visited[vertex] = True

            # Check if the destination has been reached
            if vertex == destination:
                return True

            # Explore all unvisited neighbors
            for neighbor in adj_list[vertex]:
                if not visited[neighbor]:
                    # Recursively search the neighbor if it has not been visited
                    if dfs(neighbor):
                        return True

            # Return False if no valid path was found
            return False

        # Call the recursive function starting at the source vertex
        return dfs(source)


a = Solution()

print(a.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))

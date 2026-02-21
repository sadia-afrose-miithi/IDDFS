class IterativeDeepening:
    def __init__(self):
        self.stack = []
        self.depth = 0
        self.maxDepth = 0
        self.goalFound = False
        self.finalPath = []

    def iterativeDeepening(self, grid, start, target, maxDepthLimit=50):
        self.goalFound = False
        self.finalPath = []

        self.maxDepth = 0
        while self.maxDepth <= maxDepthLimit and not self.goalFound:
            self.depth = 0
            self.stack = []
            visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

            # Depth Limited Search call
            self.depthLimitedSearch(grid, start, target, visited)

            if self.goalFound:
                print(f"Path found at depth {self.maxDepth} using IDDFS")
print(f"Traversal Order: {self.finalPath}")
                return True

            self.maxDepth += 1

        print(f"Path not found at max depth {maxDepthLimit} using IDDFS")
        return False

    def depthLimitedSearch(self, grid, source, goal, visited):
        self.stack.append(source)

        while self.stack:
            (r, c, d) = self.stack[-1]

            # goal check
            if (r, c) == goal:
                self.goalFound = True
                self.finalPath = [(x, y) for (x, y, _) in self.stack]
                return

            # depth limit reached -> backtrack
            if d == self.maxDepth:
                self.stack.pop()
                continue

            found = False

            # Move order: Down, Up, Right, Left (deterministic)
            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in moves:
                nr, nc = r + dr, c + dc

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    # 1 = free cell, 0 = wall
                    if grid[nr][nc] == 1 and visited[nr][nc] == 0:
                        visited[nr][nc] = 1
                        self.stack.append((nr, nc, d + 1))
                        found = True
                        break

            if not found:
                self.stack.pop()


if __name__ == "__main__":
    try:
        # Input format (Example):
        # rows cols
        # grid rows (e.g. 1010)
        # Start: r c
        # Target: r c

        print("Enter rows and cols:")
        rows, cols = map(int, input().strip().split())

        print("Enter grid (0=wall, 1=free):")
        grid = []
        for _ in range(rows):
            line = input().strip().replace(" ", "")
            grid.append([int(ch) for ch in line])

        print("Enter Start (row col):")
        sr, sc = map(int, input().strip().split())

        print("Enter Target (row col):")
        tr, tc = map(int, input().strip().split())

        print("Enter max depth (e.g., 6):")
        maxD = int(input().strip())

        solver = IterativeDeepening()
        solver.iterativeDeepening(grid, (sr, sc, 0), (tr, tc), maxDepthLimit=maxD)

    except ValueError:
        print("Wrong Input format")

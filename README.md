# XO Solver - Search Techniques

## Introduction

The XO Solver project focuses on solving the XO (Tic-Tac-Toe) game using six different search techniques: Depth-First Search (DFS), Breadth-First Search (BFS), Uniform Cost Search (UCS), Iterative Deepening, Bi-Directional Search, and Depth-Limited Search. The goal is to explore and compare the efficiency and performance of each technique in finding optimal solutions for the XO game.

## Search Techniques

### 1. Depth-First Search (DFS)
   - Explore the XO game tree depth-first.
   - Implement backtracking to explore deeper before backtracking.

### 2. Breadth-First Search (BFS)
   - Explore the XO game tree level by level.
   - Utilize a queue to prioritize breadth over depth.

### 3. Uniform Cost Search (UCS)
   - Expand nodes based on the cost of reaching them.
   - Prioritize nodes with lower path costs.

### 4. Iterative Deepening
   - Perform DFS with increasing depth limits until a solution is found.
   - Combine the benefits of DFS and BFS.

### 5. Bi-Directional Search
   - Conduct searches from both the initial and goal states simultaneously.
   - Merge the searches when the frontiers meet.

### 6. Depth-Limited Search
   - Set a predetermined depth limit for exploration.
   - Avoid exhaustive searches by limiting depth.
## Future Enhancements

- **Heuristic Search Techniques:**
  Explore the implementation of heuristic-based search techniques, such as A* search, to further enhance the solver's efficiency.

- **User Interface:**
  Develop a user-friendly interface to interactively play the XO game against the solver and visualize the search process.

- **Optimization:**
  Fine-tune algorithms and explore parallel computing to optimize search techniques for larger game spaces.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute. Contributions are welcome!

Happy coding and happy solving!

import numpy as np
from settings.constants import DIRECTIONS, SNAKE_BLOCK


class Snake:
    def __init__(self, head_position, direction_index, length):
        """
        @param head_position (x, y): tuple
        @param direction_index (0-3 (u, r, d, l)): int
        @param length: int
        """
        # Information snake need to know to make the move
        self.snake_block = SNAKE_BLOCK  # snake identification?
        self.current_direction_index = direction_index  # 0-3 (u, r, d, l)

        self.alive = True  # Alive identifier

        # Place the snake
        self.blocks = [head_position]  # blocks is a snake body. Init by head
        current_position = np.array(head_position)
        # building the snake body:
        # 1. Take the last position
        # 2. Add to it direction
        # 3. Add it to body at the end
        for _ in range(1, length):
            if self.current_direction_index == 0:
                current_position = [current_position[0], current_position[1] + 1]
            elif self.current_direction_index == 1:
                current_position = [current_position[0] - 1, current_position[1]]
            elif self.current_direction_index == 2:
                current_position = [current_position[0], current_position[1] - 1]
            elif self.current_direction_index == 3:
                current_position = [current_position[0] + 1, current_position[1]]
            self.blocks.append(tuple(current_position))

    def step(self, action):
        # Execute one-time step within the environment
        """
        @param action: int
        @param return: tuple, tuple
        """
        # Check if action can be performed (do nothing if in the same direction or opposite)
        cu = self.current_direction_index

        if ((cu == 0 or cu == 2) and (action == 1 or action == 3)) or ((cu == 0 or cu == 2) and (action == 1 or action == 3)):
            self.current_direction_index = action

        # Remove tail
        tail = self.blocks[len(self.blocks) - 1]
        self.blocks = self.blocks[:len(self.blocks) - 1]

        # Check new head
        if self.current_direction_index == 0:
            new_head = (self.blocks[0][0], self.blocks[0][1] - 1)
        elif self.current_direction_index == 1:
            new_head = (self.blocks[0][0] + 1, self.blocks[0][1])
        elif self.current_direction_index == 2:
            new_head = (self.blocks[0][0], self.blocks[0][1] + 1)
        elif self.current_direction_index == 3:
            new_head = (self.blocks[0][0] - 1, self.blocks[0][1])
        
        # Add new head
        self.blocks = [new_head] + self.blocks
        return new_head, tail

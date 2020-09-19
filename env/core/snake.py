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
        self.blocks = [head_position]
        current_position = np.array(head_position)
        for i in range(1, length):
            # Direction inverse of moving
            current_position = current_position - DIRECTIONS[self.current_direction_index]
            self.blocks.append(tuple(current_position))

    def step(self, action):
        # Execute one-time step within the environment
        """
        @param action: int
        @param return: tuple, tuple
        """
        # Check if action can be performed (do nothing if in the same direction or opposite)
        print(f'current_direction_index = {self.current_direction_index}, action = {action}')
        ci = self.current_direction_index

        if ((ci == 1 or ci == 3) and (action == 2 or action == 0)) or \
                ((ci == 2 or ci == 0) and (action == 1 or action == 3)):
            self.current_direction_index = action

        # Remove tail
        tail = self.blocks[len(self.blocks) - 1]
        self.blocks = self.blocks[:len(self.blocks) - 1]

        # Check new head
        if self.current_direction_index == 0:
            new_head = (self.blocks[0][0] - 1, self.blocks[0][1])
        elif self.current_direction_index == 1:
            new_head = (self.blocks[0][0], self.blocks[0][1] + 1)
        elif self.current_direction_index == 2:
            new_head = (self.blocks[0][0] + 1, self.blocks[0][1])
        elif self.current_direction_index == 3:
            new_head = (self.blocks[0][0], self.blocks[0][1] - 1)
        
        # Add new head
        self.blocks = [new_head] + self.blocks
        return new_head, tail

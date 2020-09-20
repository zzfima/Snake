from env.core.world import World
from settings.constants import DEAD_REWARD


def test_world_init():
    size = (10, 10)
    custom = True  # not random
    start_position = (3, 5)
    start_direction_index = 2
    food_position = (7, 7)
    word = World(size, custom, start_position, start_direction_index, food_position)
    assert word is not None


def test_world_food_pos():
    size = (10, 10)
    custom = True  # not random
    start_position = (3, 5)
    start_direction_index = 2
    food_position = (7, 7)
    word = World(size, custom, start_position, start_direction_index, food_position)
    assert word.food_position == food_position


def test_world_snake_pos():
    size = (10, 10)
    custom = True  # not random
    start_position = (3, 5)
    start_direction_index = 2
    food_position = (7, 7)
    word = World(size, custom, start_position, start_direction_index, food_position)
    assert word.snake.blocks == [(3, 5), (2, 5), (1, 5)]


def test_world_get_observation():
    size = (10, 10)
    custom = True  # not random
    start_position = (3, 5)
    start_direction_index = 2
    food_position = (7, 7)
    word = World(size, custom, start_position, start_direction_index, food_position)
    observation = word.get_observation()
    assert observation[3, 5] == 101
    assert observation[2, 5] == 100
    assert observation[1, 5] == 100


def test_world_move_snake_outside_bounds():
    size = (10, 10)
    custom = True  # not random
    start_position = (3, 5)
    start_direction_index = 2
    food_position = (7, 7)
    word = World(size, custom, start_position, start_direction_index, food_position)
    reward, done, snake_blocks = word.move_snake(2)
    assert word.snake.alive is True
    assert done is False
    assert reward == 0
    reward, done, snake_blocks = word.move_snake(2)
    assert word.snake.alive is True
    assert done is False
    assert reward == 0
    reward, done, snake_blocks = word.move_snake(2)
    assert word.snake.alive is True
    assert done is False
    assert reward == 0
    reward, done, snake_blocks = word.move_snake(2)
    assert word.snake.alive is True
    assert done is False
    assert reward == 0


def test_world_move_snake_eat_food():
    size = (10, 10)
    custom = True  # not random
    start_position = (3, 5)
    start_direction_index = 2
    food_position = (7, 7)
    word = World(size, custom, start_position, start_direction_index, food_position)
    reward, done, snake_blocks = word.move_snake(2)
    reward, done, snake_blocks = word.move_snake(2)
    reward, done, snake_blocks = word.move_snake(2)
    reward, done, snake_blocks = word.move_snake(2)
    reward, done, snake_blocks = word.move_snake(1)
    reward, done, snake_blocks = word.move_snake(1)
    assert word.snake.alive is True
    assert done is False
    assert reward == 1
    reward, done, snake_blocks = word.move_snake(1)


def test_world_move_snake_enter_upper_wall():
    size = (10, 10)
    custom = True  # not random
    start_position = (3, 5)
    start_direction_index = 2
    food_position = (7, 7)
    word = World(size, custom, start_position, start_direction_index, food_position)
    reward, done, snake_blocks = word.move_snake(1)
    reward, done, snake_blocks = word.move_snake(0)
    reward, done, snake_blocks = word.move_snake(0)
    reward, done, snake_blocks = word.move_snake(0)
    assert word.snake.alive is False
    assert done is True
    assert reward == DEAD_REWARD


def test_world_move_snake_enter_bottom_wall():
    size = (10, 10)
    custom = True  # not random
    start_position = (3, 5)
    start_direction_index = 2
    food_position = (7, 7)
    word = World(size, custom, start_position, start_direction_index, food_position)
    reward, done, snake_blocks = word.move_snake(1)
    reward, done, snake_blocks = word.move_snake(1)
    reward, done, snake_blocks = word.move_snake(1)
    reward, done, snake_blocks = word.move_snake(1)
    reward, done, snake_blocks = word.move_snake(1)
    reward, done, snake_blocks = word.move_snake(1)
    assert word.snake.alive is False
    assert done is True
    assert reward == DEAD_REWARD


def test_world_move_snake_enter_left_wall():
    size = (10, 10)
    custom = True  # not random
    start_position = (3, 5)
    start_direction_index = 2
    food_position = (7, 7)
    word = World(size, custom, start_position, start_direction_index, food_position)
    reward, done, snake_blocks = word.move_snake(3)
    reward, done, snake_blocks = word.move_snake(3)
    reward, done, snake_blocks = word.move_snake(3)
    reward, done, snake_blocks = word.move_snake(3)
    reward, done, snake_blocks = word.move_snake(3)
    assert word.snake.alive is False
    assert done is True
    assert reward == DEAD_REWARD


def test_world_move_snake_enter_right_wall():
    size = (10, 10)
    custom = True  # not random
    start_position = (3, 5)
    start_direction_index = 2
    food_position = (7, 7)
    word = World(size, custom, start_position, start_direction_index, food_position)
    reward, done, snake_blocks = word.move_snake(1)
    reward, done, snake_blocks = word.move_snake(1)
    reward, done, snake_blocks = word.move_snake(1)
    reward, done, snake_blocks = word.move_snake(1)
    assert word.snake.alive is False
    assert done is True
    assert reward == DEAD_REWARD

from env.core.world import World


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
    assert word.snake.blocks == [(3, 5), (3, 4), (3, 3)]


def test_world_get_observation():
    size = (10, 10)
    custom = True  # not random
    start_position = (3, 5)
    start_direction_index = 2
    food_position = (7, 7)
    word = World(size, custom, start_position, start_direction_index, food_position)
    observation = word.get_observation()
    assert observation[3, 5] == 101
    assert observation[3, 4] == 100
    assert observation[3, 3] == 100


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
    reward, done, snake_blocks = word.move_snake(2)
    assert word.snake.alive is False
    assert done is True
    assert reward == -1


def test_world_move_snake_eat_food():
    size = (10, 10)
    custom = True  # not random
    start_position = (3, 5)
    start_direction_index = 2
    food_position = (7, 7)
    word = World(size, custom, start_position, start_direction_index, food_position)
    reward, done, snake_blocks = word.move_snake(2)
    reward, done, snake_blocks = word.move_snake(2)
    reward, done, snake_blocks = word.move_snake(1)
    reward, done, snake_blocks = word.move_snake(1)
    reward, done, snake_blocks = word.move_snake(1)
    reward, done, snake_blocks = word.move_snake(1)
    assert word.snake.alive is True
    assert done is False
    assert reward == 1

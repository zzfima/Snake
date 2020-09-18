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

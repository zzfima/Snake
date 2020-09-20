from env.core.snake import Snake


def test_init():
    head_position = (3, 5)
    direction_index = 0
    length = 4
    snake = Snake(head_position, direction_index, length)
    assert snake is not None


def test_check_snake_is_up():
    head_position = (3, 5)
    direction_index = 0
    length = 4
    snake = Snake(head_position, direction_index, length)
    assert snake.blocks == [(3, 5), (4, 5), (5, 5), (6, 5)]


def test_check_snake_is_down():
    head_position = (3, 5)
    direction_index = 2
    length = 4
    snake = Snake(head_position, direction_index, length)
    assert snake.blocks == [(3, 5), (2, 5), (1, 5), (0, 5)]


def test_check_snake_is_left():
    head_position = (3, 5)
    direction_index = 3
    length = 4
    snake = Snake(head_position, direction_index, length)
    assert snake.blocks == [(3, 5), (3, 6), (3, 7), (3, 8)]


def test_check_snake_is_right():
    head_position = (3, 5)
    direction_index = 1
    length = 4
    snake = Snake(head_position, direction_index, length)
    assert snake.blocks == [(3, 5), (3, 4), (3, 3), (3, 2)]


def test_check_snake_is_down_do_steps_check_directions():
    head_position = (3, 5)
    direction_index = 2
    length = 4
    snake = Snake(head_position, direction_index, length)
    snake.step(2)
    assert snake.current_direction_index == 2
    snake.step(0)
    assert snake.current_direction_index == 2
    snake.step(1)
    assert snake.current_direction_index == 1
    snake.step(1)
    assert snake.current_direction_index == 1
    snake.step(3)
    assert snake.current_direction_index == 1


def test_check_snake_is_down_do_steps_check_blocks():
    head_position = (3, 5)
    direction_index = 2
    length = 4
    snake = Snake(head_position, direction_index, length)

    new_head, tail = snake.step(2)
    assert new_head == (4, 5)
    assert tail == (0, 5)

    new_head, tail = snake.step(2)
    assert new_head == (5, 5)
    assert tail == (1, 5)

    new_head, tail = snake.step(1)
    assert new_head == (5, 6)
    assert tail == (2, 5)

    new_head, tail = snake.step(1)
    assert new_head == (5, 7)
    assert tail == (3, 5)

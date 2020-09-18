from env.core.snake import Snake

def test_init():
    head_position = (3,5)
    direction_index = 2
    length = 4
    snake =  Snake(head_position, direction_index, length)
    assert snake.blocks == [(3, 5), (2, 5), (1, 5), (0, 5)]

import random

def get_initial_ball_velocity(speed_x, speed_y):
    """Calculate initial ball velocity with random direction"""
    return (
        speed_x * random.choice((1, -1)),
        speed_y * random.choice((1, -1))
    )

def handle_wall_collision(position, speed, boundary):
    """Handle collision with top/bottom walls"""
    if position <= 0 or position >= boundary:
        return speed * -1
    return speed
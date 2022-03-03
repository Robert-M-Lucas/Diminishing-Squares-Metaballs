class Circle:
    def __init__(self, circle_pos, r, velocity):
        self.circle_pos = circle_pos

        self.r = r

        self.velocity = velocity

    def step(self, timestep, screen_size):
        self.circle_pos[0] += self.velocity[0] * timestep
        self.circle_pos[1] += self.velocity[1] * timestep

        if self.circle_pos[0] + (self.r/2) > screen_size[0]:
            self.circle_pos[0] -= (self.circle_pos[0] + (self.r/2)) - screen_size[0]
            self.velocity[0] = - self.velocity[0]
        if self.circle_pos[0] - (self.r/2) < 0:
            self.circle_pos[0] -= (self.circle_pos[0] - (self.r/2))
            self.velocity[0] = - self.velocity[0]
        if self.circle_pos[1] + (self.r/2) > screen_size[1]:
            self.circle_pos[1] -= (self.circle_pos[1] + (self.r/2)) - screen_size[1]
            self.velocity[1] = - self.velocity[1]
        if self.circle_pos[1] - (self.r/2) < 0:
            self.circle_pos[1] -= (self.circle_pos[1] - (self.r/2))
            self.velocity[1] = - self.velocity[1]
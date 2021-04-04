class Light:
    ON = 'ON'
    OFF = 'OFF'

    def __init__(self, state):
        self._set_state(state)

    def _set_state(self, state):
        self.state = state

    @property
    def status(self):
        return self.state

    def turn_on(self):
        self._set_state(Light.ON)

    def turn_off(self):
        self._set_state(Light.OFF)

    def toggle(self):
        if self.status == Light.OFF:
            self._set_state(Light.ON)
        else:
            self._set_state(Light.OFF)

    def __repr__(self):
        return self.status


class Coordinate:
    def __init__(self, x, y):
        self.x_axis = x
        self.y_axis = y

    @property
    def x(self):
        return self.x_axis

    @property
    def y(self):
        return self.y_axis


class Panel:

    def __init__(self, size):
        self.size = size
        self.light = Light(Light.OFF)
        self.panel = self.blank_panel(size)

    @staticmethod
    def blank_row(size):
        return [Light(Light.OFF) for column in range(0, size)]

    def blank_panel(self, size):
        return [self.blank_row(size) for row in range(0, size)]

    def coordinate(self, x, y):
        return self.panel[x][y]

    def turn_on_move_right(self, y_axis, x_start, x_end):
        for col in range(x_start, x_end+1):
            self.coordinate(col, y_axis).turn_on()

    def turn_off_move_right(self, y_axis, x_start, x_end):
        for col in range(x_start, x_end+1):
            self.coordinate(col, y_axis).turn_off()

    def toogle_move_right(self, y_axis, x_start, x_end):
        for col in range(x_start, x_end+1):
            self.coordinate(col, y_axis).toggle()

    def turn_on(self, start, end):
        for row in range(start.y, end.y+1):
            self.turn_on_move_right(row, start.x, end.x)

    def turn_off(self, start, end):
        for row in range(start.y, end.y+1):
            self.turn_off_move_right(row, start.x, end.x)

    def toggle(self, start, end):
        for row in range(start.y, end.y+1):
            self.toogle_move_right(row, start.x, end.x)

    def lights_on(self):
        counter = 0
        for row in range(self.size):
            for col in range(self.size):
                if self.coordinate(row, col).status == Light.ON:
                    counter += 1
        return counter


if __name__ == "__main__":
    panel = Panel(1000)
    panel.turn_on(Coordinate(887, 9), Coordinate(959, 629))
    panel.turn_on(Coordinate(454, 398), Coordinate(844, 448))
    panel.turn_off(Coordinate(539, 243), Coordinate(559, 965))
    panel.turn_off(Coordinate(370, 819), Coordinate(676, 868))
    panel.turn_off(Coordinate(145, 40), Coordinate(370, 997))
    panel.turn_off(Coordinate(301, 3), Coordinate(808, 453))
    panel.turn_on(Coordinate(351, 678), Coordinate(951, 908))
    panel.toggle(Coordinate(720, 196), Coordinate(897, 994))
    panel.toggle(Coordinate(831, 394), Coordinate(904, 860))

    print(panel.lights_on())

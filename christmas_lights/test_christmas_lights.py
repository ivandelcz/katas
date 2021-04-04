from christmas_lights import (
    Panel,
    Light,
    Coordinate
)


def test_given_a_light_then_it_has_power_status():
    power_state = Light.OFF

    light = Light(power_state)

    assert isinstance(light, Light)
    assert light.status == power_state


def test_given_a_turn_off_light_then_it_has_turn_on_action():
    light = Light(Light.OFF)
    light.turn_on()

    assert light.status == Light.ON


def test_given_a_turn_off_light_then_it_has_turn_off_action():
    light = Light(Light.OFF)
    light.turn_off()

    assert light.status == Light.OFF


def test_given_a_turn_off_light_then_it_has_toggle_to_on_action():
    light = Light(Light.OFF)
    light.toggle()

    assert light.status == Light.ON


def test_given_a_turn_on_light_then_it_has_toggle_to_off_action():
    light = Light(Light.ON)
    light.toggle()

    assert light.status == Light.OFF


def test_given_a_turn_on_light_then_it_has_turn_off_action():
    light = Light(Light.ON)
    light.turn_off()

    assert light.status == Light.OFF


def test_given_a_coordinate_it_has_x_and_y():
    x = 0
    y = 1

    coord = Coordinate(x, y)

    assert coord.x == x
    assert coord.y == y


def test_given_a_panel_then_it_is_panel_with_set_size():
    size = 1000

    panel = Panel(size)

    assert isinstance(panel, Panel)
    assert panel.size == size


def test_given_one_cell_panel_then_it_has_one_OFF_light():
    panel = Panel(1)

    assert panel.coordinate(x=0, y=0).status == Light.OFF


def test_given_one_cell_panel_then_it_can_be_ON_light():
    panel = Panel(1)
    start_coordinate = Coordinate(0, 0)
    end_coordinate = Coordinate(0, 0)
    panel.turn_on(start_coordinate, end_coordinate)

    assert panel.coordinate(x=0, y=0).status == Light.ON


def test_given_four_cell_panel_then_it_has_four_OFF_lights():
    panel = Panel(4)

    assert panel.coordinate(0, 0).status == Light.OFF
    assert panel.coordinate(0, 1).status == Light.OFF
    assert panel.coordinate(1, 0).status == Light.OFF
    assert panel.coordinate(1, 1).status == Light.OFF


def test_given_four_cell_panel_then_power_on_first_row():
    panel = Panel(4)
    start_coordinate = Coordinate(0, 0)
    end_coordinate = Coordinate(1, 0)
    panel.turn_on(start_coordinate, end_coordinate)

    assert panel.coordinate(1, 1).status == Light.OFF
    assert panel.coordinate(0, 1).status == Light.OFF
    assert panel.coordinate(1, 0).status == Light.ON
    assert panel.coordinate(0, 0).status == Light.ON


def test_given_four_cell_panel_then_power_second_row():
    panel = Panel(4)
    start_coordinate = Coordinate(0, 1)
    end_coordinate = Coordinate(1, 1)
    panel.turn_on(start_coordinate, end_coordinate)

    assert panel.coordinate(1, 1).status == Light.ON
    assert panel.coordinate(0, 1).status == Light.ON
    assert panel.coordinate(1, 0).status == Light.OFF
    assert panel.coordinate(0, 0).status == Light.OFF


def test_given_four_cell_panel_then_power_both_rows():
    panel = Panel(4)
    start_coordinate = Coordinate(0, 0)
    end_coordinate = Coordinate(1, 1)
    panel.turn_on(start_coordinate, end_coordinate)

    assert panel.coordinate(0, 0).status == Light.ON
    assert panel.coordinate(0, 1).status == Light.ON
    assert panel.coordinate(1, 0).status == Light.ON
    assert panel.coordinate(1, 1).status == Light.ON


def test_given_four_cell_panel_then_power_on_first_row_and_toggle_all_panel():
    panel = Panel(4)
    panel.turn_on(Coordinate(0, 0), Coordinate(1, 0))
    panel.toggle(Coordinate(0, 0), Coordinate(1, 1))

    assert panel.coordinate(1, 1).status == Light.ON
    assert panel.coordinate(0, 1).status == Light.ON
    assert panel.coordinate(1, 0).status == Light.OFF
    assert panel.coordinate(0, 0).status == Light.OFF


def test_given_four_cell_panel_then_power_on_and_then_off():
    panel = Panel(4)
    panel.turn_on(Coordinate(0, 0), Coordinate(1, 0))
    panel.turn_off(Coordinate(0, 0), Coordinate(1, 1))

    assert panel.coordinate(0, 0).status == Light.OFF
    assert panel.coordinate(0, 1).status == Light.OFF
    assert panel.coordinate(1, 0).status == Light.OFF
    assert panel.coordinate(1, 1).status == Light.OFF


def test_given_four_cell_panel_and_power_on_second_row_then_two_lights_on():
    panel = Panel(4)
    start_coordinate = Coordinate(0, 1)
    end_coordinate = Coordinate(1, 1)
    panel.turn_on(start_coordinate, end_coordinate)

    assert panel.lights_on() == 2


def test_given_four_cell_panel_and_power_on_all_then_four_lights_on():
    panel = Panel(4)
    start_coordinate = Coordinate(0, 0)
    end_coordinate = Coordinate(1, 1)
    panel.turn_on(start_coordinate, end_coordinate)

    assert panel.lights_on() == 4

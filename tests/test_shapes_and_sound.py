import pytest


def test_shapes_and_sound_no_input(capfd):
    import src.shapes_and_sound as obj_under_test
    obj_under_test.just_for_test()

    out, err = capfd.readouterr()
    assert out == "TODO"


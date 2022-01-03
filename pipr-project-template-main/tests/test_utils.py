from password_generator.utils import get_random_number


def test_get_random_number():
    assert get_random_number() == 4

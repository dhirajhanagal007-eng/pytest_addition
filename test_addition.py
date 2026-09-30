from add import calculate_add   

def test_positive_numbers():
    assert calculate_add(20, 40) == 60

    def test_zero_numbers():
        assert calculate_add(50, 0) == 50

        def test_negative_numbers():
            assert calculate_add(-50, -10) == -40
def test_is_one_of_instance_of():
    assert is_one_of_instance_of(int, [int, str])
    assert is_one_of_instance_of(int, [str, int])
    assert not is_one_of_instance_of(str, [int, int])

def is_one_of_instance_of(obj:object, types:list):
    instance_found = False
    for type in types:
        if obj == type or isinstance(obj, type):
            instance_found = True
            break

    return instance_found
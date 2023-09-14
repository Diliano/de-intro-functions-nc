# Exercise 1
def test_multi_type_list():
    multi_type_list = ["I am a string", 42, True, [1, 2, 3]]

    assert type(multi_type_list[0]) == FILL_ME_IN
    assert type(multi_type_list[1]) == FILL_ME_IN
    assert type(multi_type_list[2]) == FILL_ME_IN
    assert type(multi_type_list[3]) == FILL_ME_IN


# Exercise 2
def test_list_mutation():
    letters = ["a", "b", "c"]
    letters.append("d")
    letters.append("g")

    assert letters == FILL_ME_IN

    last_letter = letters.pop()

    assert last_letter == FILL_ME_IN
    assert letters == FILL_ME_IN


# Exercise 3
def test_nested_lists():
    rows = [
        ["a", "b", "c"],
        ["d", "e", "f"],
        ["g", "h", "i"],
    ]

    assert rows[0] == FILL_ME_IN
    assert rows[1] == FILL_ME_IN
    assert rows[2] == FILL_ME_IN

    first_row = rows[0]
    assert first_row[0] == "a"
    assert first_row[FILL_ME_IN] == "b"

    assert rows[1][FILL_ME_IN] == "e"
    assert rows[2][FILL_ME_IN] == "g"
    assert rows[0][FILL_ME_IN] == "c"


# Exercise 4
def test_dictionary_keys():
    father = {
        "first_name": "Michael",
        "last_name": "Bluth",
        "age": 33,
    }

    key = "first_name"
    assert father["last_name"] == FILL_ME_IN
    assert father["age"] == FILL_ME_IN
    assert father[key] == FILL_ME_IN


# Exercise 5
def test_removing_dict_keys():
    brother_in_law = {
        "name": "Tobias",
        "lastname": "Funke",
        "job": "therapist",
    }

    assert brother_in_law["job"] == FILL_ME_IN

    del brother_in_law["job"]
    assert brother_in_law == FILL_ME_IN


# Exercise 6
def test_nested_dictionaries():
    bluth_family = {
        "father": {
            "name": "George",
        },
        "mother": {
            "name": "Lucille",
        },
        "sons": [{"name": "GOB"}, {"name": "Michael"}, {"name": "Buster"}],
        "daughters": [{"name": "Lindsay"}],
    }

    assert bluth_family["father"]["name"] == FILL_ME_IN
    assert bluth_family["mother"]["name"] == FILL_ME_IN
    assert bluth_family["daughters"][FILL_ME_IN][FILL_ME_IN] == "Lindsay"

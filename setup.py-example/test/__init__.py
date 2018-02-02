from unittest import mock


def test_main_exists():
    # from .. import main
    import main
    print("Running main")
    assert main, "It exists"


def test_main_module_has_output_saying_method():
    import main

    print(dir(main))

    assert main.output_saying, "main.output_saying not found"


@mock.patch('main.output_saying')
def test_hello_calls_output_func(output_saying_mock):
    import main

    main.hello()

    output_saying_mock.assert_called()


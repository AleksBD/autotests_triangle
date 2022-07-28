from src.pages.triangle import TrianglePage


testcase_parameters = [
    (7, 7, 7, 'Это равносторонний треугольник.\nВы ввели:\nA: 5; B: 5; C: 5'),
    (5, 5, 1, 'Это равнобедренный треугольник.\nВы ввели:\nA: 5; B: 5; C: 1'),
    (4, 3, 5, 'Это прямоугольный треугольник.\nВы ввели:\nA: 4; B: 3; C: 5'),
    (2, 4, 5, 'Это тупоугольный треугольник.\nВы ввели:\nA: 2; B: 4; C: 5'),
    (5, 5, 7.07, 'Это прямоугольный треугольник.\nВы ввели:\nA: 5; B: 5; C: 7.07'),
]


def check_test_case(driver, side_a_value, side_b_value, side_c_value, expected_result):
    triangle_page = TrianglePage(driver)

    triangle_page.open_page()
    triangle_page.fill_side(triangle_page.side_a_selector, side_a_value)
    triangle_page.fill_side(triangle_page.side_b_selector, side_b_value)
    triangle_page.fill_side(triangle_page.side_c_selector, side_c_value)
    triangle_page.click_check_button()

    actual_result = triangle_page.get_text_field_value()
    try:
        assert actual_result == expected_result
        print('test pass')

    except AssertionError:
        print('test falled')

    triangle_page.clear_fields()


def run(driver):
    for param_set in testcase_parameters:
        check_test_case(driver, *param_set)

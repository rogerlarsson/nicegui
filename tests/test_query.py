from nicegui import ui

from .screen import Screen


def test_query_body(screen: Screen):
    ui.label('Hello')
    ui.query('body').classes('bg-orange-100')
    ui.button('Red background', on_click=lambda: ui.query('body').classes(replace='bg-red-100'))
    ui.button('Blue background', on_click=lambda: ui.query('body').classes(replace='bg-blue-100'))
    ui.button('Small padding', on_click=lambda: ui.query('body').style('padding: 1px'))
    ui.button('Large padding', on_click=lambda: ui.query('body').style('padding: 10px'))
    ui.button('Data X = 1', on_click=lambda: ui.query('body').props('data-x=1'))
    ui.button('Data X = 2', on_click=lambda: ui.query('body').props('data-x=2'))

    screen.open('/')
    screen.should_contain('Hello')
    assert screen.find_by_tag('body').get_attribute('class') == 'desktop no-touch body--light bg-orange-100'

    screen.click('Red background')
    screen.wait(0.5)
    assert screen.find_by_tag('body').get_attribute('class') == 'desktop no-touch body--light bg-red-100'

    screen.click('Blue background')
    screen.wait(0.5)
    assert screen.find_by_tag('body').get_attribute('class') == 'desktop no-touch body--light bg-blue-100'

    screen.click('Small padding')
    screen.wait(0.5)
    assert screen.find_by_tag('body').value_of_css_property('padding') == '1px'

    screen.click('Large padding')
    screen.wait(0.5)
    assert screen.find_by_tag('body').value_of_css_property('padding') == '10px'

    screen.click('Data X = 1')
    screen.wait(0.5)
    assert screen.find_by_tag('body').get_attribute('data-x') == '1'

    screen.click('Data X = 2')
    screen.wait(0.5)
    assert screen.find_by_tag('body').get_attribute('data-x') == '2'


def test_query_multiple_divs(screen: Screen):
    ui.label('A')
    ui.label('B')
    ui.button('Add border', on_click=lambda: ui.query('div').style('border: 1px solid black'))

    screen.open('/')
    screen.click('Add border')
    screen.wait(0.5)
    assert screen.find('A').value_of_css_property('border') == '1px solid rgb(0, 0, 0)'
    assert screen.find('B').value_of_css_property('border') == '1px solid rgb(0, 0, 0)'

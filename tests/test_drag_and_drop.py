from libraries.library_drag_and_drop import DragDrop
import pytest


@pytest.mark.skip("HTML drag and drop not supported by selenium. Hence skipping.")
def test_drag_and_drop(open_browser):
    driver = open_browser
    url = "http://the-internet.herokuapp.com/drag_and_drop"
    class_dragdrop_instance = DragDrop(driver, url)
    class_dragdrop_instance.move_a_to_b()

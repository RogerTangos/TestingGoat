from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit an empty
        # list item. She hits Enter on the empty input box

        # The home page refreshes and shows her an error message saying
        # that list items can't be blank

        # She tries again, actually using text for the item, which now works

        # Perversely, she tries to submit a second blank list item

        # The site shows her a similar warning on the list page

        # She can correct it by filling some text in.
        self.fail('write me!')

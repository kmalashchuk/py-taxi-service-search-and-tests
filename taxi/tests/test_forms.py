from django.test import TestCase
from taxi.forms import DriverSearchForm, CarSearchForm, ManufacturerSearchForm


class SearchFormTests(TestCase):
    def test_driver_search_form_valid_data(self):
        form = DriverSearchForm(data={"title": "Petrenko"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["title"], "Petrenko")

    def test_driver_search_form_empty_data(self):
        form = DriverSearchForm(data={})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["title"], "")

    def test_driver_search_form_placeholder(self):
        form = DriverSearchForm()
        self.assertEqual(
            form.fields["title"].widget.attrs["placeholder"],
            "Search by name"
        )

    def test_car_search_form_placeholder(self):
        form = CarSearchForm()
        self.assertEqual(
            form.fields["title"].widget.attrs["placeholder"],
            "Search by car"
        )

    def test_manufacturer_search_form_placeholder(self):
        form = ManufacturerSearchForm()
        self.assertEqual(
            form.fields["title"].widget.attrs["placeholder"],
            "Search by model"
        )

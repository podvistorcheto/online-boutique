from django import forms
from .models import Order


class Orderform(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name',
                  'email',
                  'phone_number',
                  'street_address1',
                  'street_address2',
                  'town_or_city',
                  'postcode',
                  'country',
                  'county',)

        """ First we call the default init method to set the form up as it would be by default."""

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }
        """
        Next we're setting the autofocus attribute on the full name field to true
        so the cursor will start in the full name field when the user loads the page.
        """
        self.fields['full_name'].widget.attrs['autofocus'] = True
        """
        Next we're setting the autofocus attribute on the full name field to true
        so the cursor will start in the full name field when the user loads the page.
        """
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
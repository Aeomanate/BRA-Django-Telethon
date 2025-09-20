from django import forms

class OrderFilterForm(forms.Form):
    start_date = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "px-3 py-2 rounded bg-gray-800 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
            }
        )
    )
    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "px-3 py-2 rounded bg-gray-800 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
            }
        )
    )

    min_volume = forms.FloatField(required=False, label="Мінімальний обʼєм (мм³)")
    max_volume = forms.FloatField(required=False, label="Максимальний обʼєм (мм³)")
    min_price = forms.FloatField(required=False, label="Мінімальна ціна (USD)")
    max_price = forms.FloatField(required=False, label="Максимальна ціна (USD)")
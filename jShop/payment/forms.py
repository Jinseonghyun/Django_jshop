from django import forms
from .models import ShippingAddress


class ShippingForm(forms.ModelForm):

    shipping_full_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "이름"}),
        required=True,
    )

    shipping_email = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "이메일 주소"}
        ),
        required=True,
    )

    shipping_address1 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "주소"}),
        required=True,
    )

    shipping_address2 = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "상세주소"}
        ),
        required=True,
    )

    shipping_city = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "시"}),
        required=True,
    )

    shipping_state = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "주"}),
        required=False,
    )

    shipping_zipcode = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "우편번호"}
        ),
        required=False,
    )

    shipping_country = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "국가"}),
        required=True,
    )

    class Meta:
        model = ShippingAddress
        fields = [
            "shipping_full_name",
            "shipping_email",
            "shipping_address1",
            "shipping_address2",
            "shipping_city",
            "shipping_state",
            "shipping_zipcode",
            "shipping_country",
        ]

        exclude = ["user"]

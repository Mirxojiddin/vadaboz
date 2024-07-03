
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from accounts.models import CustomUser, Province, District, City


class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'user_photo', 'province', 'district', 'city',
                  'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['district'].queryset = District.objects.none()
        self.fields['city'].queryset = City.objects.none()

        if 'province' in self.data:
            try:
                province_id = int(self.data.get('province'))
                self.fields['district'].queryset = District.objects.filter(province_id=province_id).order_by('name')
            except (ValueError, TypeError):
                pass  # Invalid input; ignore and fallback to empty district queryset

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['city'].queryset = City.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # Invalid input; ignore and fallback to empty city queryset

        elif self.instance.pk:
            self.fields['district'].queryset = self.instance.province.district_set.order_by('name')
            self.fields['city'].queryset = self.instance.district.city_set.order_by('name')


class CustomUserUpdateForm(UserChangeForm):
    password = None  # Remove the password field

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'user_photo', 'province', 'district', 'city']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['district'].queryset = District.objects.none()
        self.fields['city'].queryset = City.objects.none()

        if 'province' in self.data:
            try:
                province_id = int(self.data.get('province'))
                self.fields['district'].queryset = District.objects.filter(province_id=province_id).order_by('name')
            except (ValueError, TypeError):
                pass  # Invalid input; ignore and fallback to empty district queryset

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['city'].queryset = City.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # Invalid input; ignore and fallback to empty city queryset

        elif self.instance.pk:
            self.fields['district'].queryset = self.instance.province.district_set.order_by('name')
            self.fields['city'].queryset = self.instance.district.city_set.order_by('name')


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'province', 'district', 'city', 'is_staff',
                  'is_active', 'is_superuser', 'groups', 'user_permissions']

    class Media:
        js = ('/js/custom_user.js',)



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UserCustomCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'student_id', 'address', 'gender',)
        
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import View, TemplateView
from .forms import SignUpForm
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin

UserModel = get_user_model()


# Sign Up View
class SignUpView(SuccessMessageMixin, View):
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password != confirm_password:
                messages.error(self.request, "password and confirm password does not matching")
                return redirect('account:signup')

            phone = form.cleaned_data['phone']
            user = UserModel.objects.create(first_name=first_name, last_name=last_name, email=email, password=password,
                                            phone=phone)
            user.set_password(password)
            user.is_active = True
            user.verified = True
            user.save()
            messages.success(self.request, "Signup successful! please login")
            return redirect('account:signup')
        return render(request, self.template_name, {'form': form})


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

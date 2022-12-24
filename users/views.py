from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST) # данные которые ввел пользователь
        if form.is_valid(): # нет ли никаких ошибок при вводе в форму при  регистрации
            form.save()
            username = form.cleaned_data.get('username') # содержит значение которое ввел пользователь в форму username
            messages.success(request, f'Your account has been created') # чтобы ошибка выводилась
            return redirect('login') # после введения данных переходит на главную страницу home
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'register_form': form})


@login_required()
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                               request.FILES,
                               instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account updated successfully')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


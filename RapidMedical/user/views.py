from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, HospitalProfileUpdateForm, HospitalInfoForm
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import account_activation_token
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from .models import Profile



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            mail = form.cleaned_data.get('email')
            form.save()

            userr = User.objects.get(username=username)


            uidb64 = urlsafe_base64_encode(force_bytes(userr.pk))

            domain = get_current_site(request).domain
            link = reverse('activate',kwargs={'uidb64': uidb64, 'token': account_activation_token.make_token(userr)})
            activate_url = 'http://' + domain + link
            email_subject = 'Activate your account'
            email_body = 'Hello {0} thanks for signing up with us, please use this link to verify your account \n {1}'.format(
                username, activate_url)

            email = send_mail(email_subject, email_body, 'Noreply@FX.com', [mail], fail_silently= False)
            messages.success(request, f'Congrats {username}, Your account was created successfully')

            return redirect('verify')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})




    
def verify_mail(request):
    return render(request, 'user/verify.html')

def Hospitalprofile(request):
    return render(request, 'user/HospitalProfile.html')




#def profile(request):
 #   return render(request, 'user/profile.html')

def UpdateProfile(request, profileId):
    p = User.objects.get(id=profileId)
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
        request.FILES,
        instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account Update Successful!')
            return redirect(reverse('profileview', args=[p.id]))
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'user/profileUpdate.html', context)

def profileView(request, profileId):
    p = User.objects.get(id=profileId)

    return render(request, 'user/profileView.html', context={'user': p})


def HospitalUpdateProfile(request, profileId):
    u = get_object_or_404(klass=User,id=profileId)

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        h_form = HospitalProfileUpdateForm(request.POST,
        request.FILES,
        instance=request.user.profile)
        p_form = ProfileUpdateForm(request.POST,
        request.FILES,
        instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account Update Successful!')
            return redirect(reverse('profileview', args=[u.id]))
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        h_form = HospitalProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'h_form': h_form
    }
    return render(request, 'user/HospitalprofileUpdate.html', context)

def hospitalinfo(request):
    if request.method == "POST":
        p_form = HospitalInfoForm(request.POST,
        request.FILES,
        instance=request.user)
        if p_form.is_valid():
            userr= p_form.cleaned_data['user'] 
            print(userr)
            p_form.save(commit=True)

            messages.success(request, f'Hospital Details Created Successfully!')
            return redirect(reverse('profileview', args=[request.user.id]))
    else:
        p_form = HospitalInfoForm(instance=request.user)

    context = {
        'p_form': p_form
    }
    return render(request, 'user/Hospitalregister.html', context)


    
class verification(View):
    def get(self, request, uidb64, token):

        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('login' + '?message' + 'User already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')
        except Exception as e:
            pass
        return redirect('login')
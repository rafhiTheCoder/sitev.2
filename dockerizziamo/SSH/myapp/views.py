from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import Add
from .models import Serra

# Create your views here.

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")


"""
@login_required
def dashboard(request):
    user_serra_objects = request.user.serra.all()
    serra_codex = [serra.code for serra in user_serra_objects]

    # Fill the list with empty strings to ensure it has 10 elements
    serra_codes = serra_codex + [""] * (10 - len(serra_codex))

    # Print the codes (for debugging purposes)
    print(serra_codes)
    
    return render(request, "dashboardMulti.html", {"serra_codes": serra_codes})
"""




@login_required
def dashboard(request):
    #X70odAJONACz86q40l7MdtfauLgpPMga39oao-_ImlcKUKzV7uLyqhQXdSr6cuWqhbLilpv2pniPPuo46PadAA==
    user_serra_objects = request.user.serra.all()


    serra_codex = [serra.code for serra in user_serra_objects]

    serra_codes=["","","","","","","","","",""]

    # Extract the code attribute from each Serra object
    for i in range(10):
        try:
            serra_codes[i]=serra_codex[i]
        except:
            serra_codes[i]=""


    # Print the codes (for debugging purposes)
    print(serra_codes)
    
    return render(request,"dashboard.html", {"var" : serra_codes[0],"var1" : serra_codes[1],"var2" : serra_codes[2],
                                             "var3" : serra_codes[3],"var4" : serra_codes[4],"var5" : serra_codes[5],
                                               "var6" : serra_codes[6],"var7" : serra_codes[7],"var8" : serra_codes[8],"var9" : serra_codes[9]})
@login_required
def serre(request):
    if request.method == "POST":
        form = Add(request.POST)
        if form.is_valid():
            n = form.cleaned_data["code"]
            
            # Check if the code is already associated with any user
            if Serra.objects.filter(code=n).exists():
                # Check if the code is associated with the current user
                if Serra.objects.filter(code=n, user=request.user).exists():
                    form.add_error('code', 'You have already added this code.')
                else:
                    form.add_error('code', 'This code is already used by another user.')
            # Check if the user already has 10 codes
            elif Serra.objects.filter(user=request.user).count() >= 10:
                form.add_error('code', 'You cannot add more than 10 codes.')
            else:
                t = Serra(code=n, user=request.user)
                t.save()
                return redirect('serre')  # Redirect to the same page to clear the form
    else:
        form = Add()
    
    return render(request, "serre.html", {"form": form})

@login_required
def delete_serra(request, serra_id):
    serra = get_object_or_404(Serra, pk=serra_id, user=request.user)
    if request.method == 'POST':
        serra.delete()
        return redirect('serre')
    return render(request, 'confirm_delete.html', {'serra': serra})


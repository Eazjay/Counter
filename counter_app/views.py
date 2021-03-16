from django.shortcuts import render, redirect

def counter(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1
    count = request.session['counter']
    print(f"You visited the site {count} times!")
    return render(request, 'counter.html')

def add_2_counter(request):
    request.session['counter'] += 1
    count = request.session['counter']
    print(f"You visited the site {count} times!")
    return redirect('/')

def delete_session(request):
    del request.session['counter']
    return redirect('/')


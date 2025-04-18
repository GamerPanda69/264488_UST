from django.shortcuts import render
import random

def salary_form(request):
    return render(request, 'salary_app/form.html')

def calculate_salary(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        company = request.POST.get('company')
        gross_salary = float(request.POST.get('gross_salary', 0))
        tax = float(request.POST.get('tax', 0))
        bonus = float(request.POST.get('bonus', 0))

        net_salary = gross_salary - (gross_salary * (tax / 100)) + (gross_salary * (bonus / 100))

        context = {
            'name': name,
            'net_salary': round(net_salary, 2),
        }
        return render(request, 'salary_app/result.html', context)
    return render(request, 'salary_app/form.html')

def jumble_word(request):
    jumbled = ''
    word = ''
    if request.method == 'POST':
        word = request.POST.get('word', '')
        word_list = list(word)
        random.shuffle(word_list)
        jumbled = ''.join(word_list)

    return render(request, 'salary_app/jumble.html', {'original': word, 'jumbled': jumbled})

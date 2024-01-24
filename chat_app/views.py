from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import openai


def home(request):
    return render(request, 'chat_app/home.html')


openai.api_key = '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'


# @login_required()
def get_completion(prompt):
    print(prompt)
    query = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = query.choices[0].text
    print(response)
    return response


def query_view(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        response = get_completion(prompt)
        return JsonResponse({'response': response})
    return render(request, 'chat_app/home.html')

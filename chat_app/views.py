from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from openai import OpenAI


def home(request):
    return render(request, 'chat_app/home.html')


# @login_required()
# openai.api_key = ''  # Replace with your OpenAI API key

client = OpenAI(api_key="")


def get_completion(prompt):
    print(prompt)
    query = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Use the latest engine
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=1024,
        stop=None,
        temperature=0.5,
    )

    response = query.choices[0].message["content"]
    print(response)
    return response


def query_view(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        response = get_completion(prompt)
        return JsonResponse({'response': response})
    return render(request, 'chat_app/home.html')

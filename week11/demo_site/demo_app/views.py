from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from demo_app.models import Event, KeyWord
from json import dumps, loads
from django.http import HttpResponse


def index(request):
    context = RequestContext(request)
    # latest = Event.objects.all().order_by('-from_date_time')[:5]
    words = KeyWord.objects.all()
    matches = {}
    print(request.POST)
    if request.method == "POST":
        for w in words:
            key = "w" + str(w.id)
            if request.POST.has_key(key):
                word = w.word
                matches[word] = Event.objects.extra(
                    where=[
                        " title LIKE '%" + word + "%' " +
                        " OR summary LIKE '%" + word + "%' " +
                        " OR description LIKE '%" + word + "%' "
                    ]
                )
        events = []
    if len(matches) == 0:
        events = Event.objects.all()

    print matches

    context_dict = {
        'events': events,
        'words': words,
        'matches': matches,
    }
    return render(request, 'demo_app/list.html', context_dict)


def ajax(request):
    # latest = Event.objects.all().order_by('-from_date_time')[:5]
    words = list(KeyWord.objects.all())
    matches = {}
    print(request.POST)
    if request.method == "POST":
        for w in words:
            key = "w" + str(w.id)
            if request.POST.has_key(key):
                word = w.word
                matches[word] = list(Event.objects.extra(where=["title LIKE '%" + word + "%'"]))
        events = []
    if len(matches) == 0:
        events = list(Event.objects.all())

    print matches
    event_list = []
    for e in events:
        event_list.append({
            "title": e.title,
            "summary": e.summary,
            "description": e.description,
        })
    word_list = []
    for w in words:
        word_list.append({
            "word": w.word
        })
    context = {
        'events': event_list,
        'words': word_list,
        'matches': matches,
    }
    json_response = dumps(context)
    return HttpResponse(json_response, content_type="application/json")


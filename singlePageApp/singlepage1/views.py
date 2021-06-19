from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "singlepage1/index.html")

# The texts are much longer in reality, but have
# been shortened here to save space
# texts = ["Text 1", "Text 2", "Text 3"]
texts = ["Lorem ipsum dolor sit amet consectetur adipisicing elit.",
"Quis, itaque? Ullam placeat praesentium quaerat veritatis reiciendis sint nesciunt sunt",
"assumenda possimus fugit ipsum minima distinctio eos, culpa necessitatibus reprehenderit doloremque."
]


def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")
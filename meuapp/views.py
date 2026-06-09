from django.shortcuts import render

def index(request):
    nome = request.GET.get("nome")
    contexto = {
        "nome": nome
    }
    return render(request, "index.html", contexto)

def contato(request):
    return render(request, "contato.html")

def aluno(request, id_aluno):
    contexto = {
        "id_aluno": id_aluno,   
    }
    return render(request, "aluno.html", contexto)
from django.shortcuts import render

# Create your views here.
def index(request):
    obras = [
        {   
            'titulo': 'Interestelar',
            'tipo': 'Filme',
            'imagem': 'https://upload.wikimedia.org/wikipedia/pt/thumb/3/3a/Interstellar_Filme.png/250px-Interstellar_Filme.png' 
        },
        {
            'titulo': 'Stanger Things',
            'tipo': 'Série',
            'imagem': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtW_fEtl3nUNKYfCyQxAA0Z9DhdSvjQzj9gg&s' 
        },
    ]

    context = {'obras': obras}

    return render(request, "catalogo/index.html", context)


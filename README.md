# Projetao1

Em "paseo":<br>

   "settings.py " = mudei a lingua e o fuso-horário, coloquei as aplicações no "INSTALLED_APPS"
   para ele reconhecer o "app", bem como o "bootsrapfom" instalado pelo terminal para renderizar os formulários nos templates<br> 
    "ruls.py": importei 'path' e 'include' para incluir as Urls de "app" nas princiapis 
    
Em "app":<br>
    "static" : coloquei os CSS do bootstrap <br>
    "templates": criei os Htmls de cada página<br> 
    "migrations": criada automaticamente prar mostrar a migração pro Admin<br> 
    "models.py": criei o modelo de usuário de acordo com a documentação Django original <br> 
    "forms.py": criei o diretório e nele transformei o modelo User num formulário para receber o input em cadastro.html <br> 
    "admin.py" : coloquei o modelo User como modelo no Admin 
    "urls.py" : listei os caminhos dos htmls
    "views.py" : atribui os caminhos das htmls e defini atribuí ao 'cadatsro.html" os inouts do formulário 
    
    
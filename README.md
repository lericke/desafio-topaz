# desafio-topaz

Repositório com as funcionalidades pedidas no teste prático.

## Passo a passo de uso do projeto
------
1° Clonar o projeto 
```
git clone git@github.com:lericke/desafio-topaz.git
```
2° Instalar as dependências / Dentro do projeto
```
pip3 install -r requirements.txt
```
3° Rodar o projeto 
```
uvicorn main:app --reload
```

### Como gerar o relatorio do usuario git.

Acessar o localhost [http://localhost:8000/docs](http://localhost:8000/docs) e no endpoint /gera_relatorio, passar o username do perfil do github para qual desejar gerar o relatório, o arquivo do relatório será gerado dentro da pasta app no projeto.

# OBSERVAÇÃO.

Por não possuir experiência com o desenvolvimento de testes, acabei tendo dificuldades na implementação dos mesmo, e não consegui entregar essa etapa completa.

Obrigado pela oportunidade!


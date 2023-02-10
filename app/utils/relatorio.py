

class Relatorio:

    def criar_relatorio(self, username, dados_usuario: dict, repositorios: dict):
        
        # Dados do Usuario
        nome = dados_usuario.get('name')
        perfil = dados_usuario.get('identificar o que se encaixa melhor em perfil ')
        numero_repositorios_publicos = dados_usuario.get('public_repos')
        numero_seguidores = dados_usuario.get('followers')
        numeros_seguidos = dados_usuario.get('following')

        filename = f"{username}.txt"

        f = open(f"{filename}", "a")

        f.write(f"Nome: {nome}\n")
        f.write(f"Pefil: {perfil}\n")
        f.write(f"Número de repositórios publicos: {numero_repositorios_publicos}\n")
        f.write(f"Número de seguidores: {numero_seguidores}\n")
        f.write(f"Numero de usuarios seguidos: {numeros_seguidos}\n")
        

        # usuario = f"nome: {nome}\n"
        # usuario += f"Perfil: {perfil}\n"
        # usuario += f"Número de repositórios publicos: {numero_repositorios_publicos}\n"
        # usuario += f"Número de seguidores: {numero_seguidores}\n"
        # usuario += f"Número de usuários seguidos: {numeros_seguidos}\n"
        f.write("Lista de repositorios publicos: ")
        
        
        # Repositorios
        repos = []

        for repo in repositorios:
            repos.append(repo.get("name"))
            f.write(repo.get("name")+", ")


        f.close()
        
        return True
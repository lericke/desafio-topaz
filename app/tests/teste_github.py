import unittest

from utils.github import GitHub

resposta_usuario = {'login': 'lericke', 'id': 77762679, 'node_id': 'MDQ6VXNlcjc3NzYyNjc5', 'avatar_url': 'https://avatars.githubusercontent.com/u/77762679?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/lericke', 'html_url': 'https://github.com/lericke', 'followers_url': 'https://api.github.com/users/lericke/followers', 'following_url': 'https://api.github.com/users/lericke/following{/other_user}', 'gists_url': 'https://api.github.com/users/lericke/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/lericke/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/lericke/subscriptions', 'organizations_url': 'https://api.github.com/users/lericke/orgs', 'repos_url': 'https://api.github.com/users/lericke/repos', 'events_url': 'https://api.github.com/users/lericke/events{/privacy}', 'received_events_url': 'https://api.github.com/users/lericke/received_events', 'type': 'User', 'site_admin': False, 'name': 'Erick Araujo', 'company': None, 'blog': '', 'location': None, 'email': None, 'hireable': None, 'bio': 'Desenvolvedor BackEnd Python.', 'twitter_username': None, 'public_repos': 8, 'public_gists': 0, 'followers': 0, 'following': 0, 'created_at': '2021-01-21T01:43:38Z', 'updated_at': '2023-02-11T04:10:23Z'}


class TestGithub(unittest.TestCase):
    

    def test_get_usuario_data(self):
        
        self.assertEqual(GitHub().get_data("lericke"), resposta_usuario)


if __name__ == '__name__':
    unittest.main()
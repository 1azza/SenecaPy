import Seneca

token = Seneca.token.Refresh('AIzaSyDXmCdeFZFJbQOtl6xupkxZw-lIOKuJQKg')
user = Seneca.User(token)
print(f'Found User:\n{user.displayName}')



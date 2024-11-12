# Lista över användarnamn och deras korrekta lösenord
user_credentials = {
    "user1": "Password123",
    "admin": "Admin@2023",
    "user2": "Welcome123",
    "guest": "Guest1234"
}

# En lista över vanligt använda lösenord
password_list = ["Password123", "123456", "Welcome123", "Guest1234", "password"]

"""
Ladda ner password_spraying.py från uppgiftsmaterial.
Kontrollera om någon utav lösenorden i password_list matchar lösenordet för en user i user_credentials
Skriv resultatet till fil (och i konsolen) med varje lösenord per user och om det lyckades eller inte.
Exempel: 
user1: 123456 -> failed
user1: Welcome123 -> failed
"""

with open("spray.txt", "w") as file:
    for username in user_credentials.keys():
        for password in password_list:
            if password == user_credentials[username]:
                result = "success"
            else:
                result = "failed"
            
            file.write(f"{username}: {password} => {result}\n")
            print(f"{username}: {password} => {result}")
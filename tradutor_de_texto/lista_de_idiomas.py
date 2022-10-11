#criar uma lista de idiomas

lista_idiomas =['Ingles', 'Espanhol', 'Frances', 'Italiano', 'Alemao', 'Portugues', 'Russo', 'Chines', 'Japones',
                'Coreano', 'Arabe', 'Turco', 'Hindi', 'Indonesio', 'Vietnamita', 'Filipino', 'Thai', 'Malay',
                'Bengali', 'Urdu', 'Tamil', 'Persa', 'Javanês', 'Mandarim', 'Cantonês', 'Sueco', 'Norueguês',
                'Dinamarquês', 'Holandês', 'Finlandês', 'Polonês', 'Eslovaco', 'Esloveno', 'Catalão', 'Galego',
                'Basco', 'Galês', 'Córnico', 'Bretão', 'Alemão', 'Inglês', 'Francês', 'Espanhol', 'Italiano',
                'Português', 'Russo', 'Chinês', 'Japonês', 'Coreano', 'Árabe', 'Turco', 'Hindi', 'Indonésio',
                'Vietnamita', 'Filipino', 'Thai', 'Malay', 'Bengali', 'Urdu', 'Tamil', 'Persa', 'Javanês', 'Mandarim',
                'Cantonês', 'Sueco', 'Norueguês', 'Dinamarquês', 'Holandês', 'Finlandês', 'Polonês', 'Eslovaco',
                'Esloveno', 'Catalão', 'Galego', 'Basco', 'Galês', 'Córnico', 'Bretão', 'Alemão', 'Inglês', 'Francês',
                'Espanhol', 'Italiano', 'Português', 'Russo', 'Chinês', 'Japonês', 'Coreano', 'Árabe', 'Turco',
                'Hindi', 'Indonésio', 'Vietnamita', 'Filipino', 'Thai', 'Malay', 'Bengali', 'Urdu', 'Tamil', 'Persa',
                'Javanês', 'Mandarim', 'Cantonês', 'Sueco', 'Norueguês', 'Dinamarquês', 'Holandês', 'Finlandês',
                'Polonês', 'Eslovaco', 'Esloveno', 'Catalão', 'Galego', 'Basco', 'Galês', 'Córnico', 'Bretão',
                'Alemão', 'Inglês', 'Francês', 'Espanhol', 'Italiano', 'Português', 'Russo', 'Chinês', 'Japonês',
                'Coreano', 'Árabe', 'Turco', 'Hindi', 'Indonésio', 'Vietnamita', 'Filipino', 'Thai', 'Malay',
                'Bengali', 'Urdu', 'Tamil', 'Persa', 'Javanês', 'Mandarim', 'Cantonês', 'Sueco', 'Norueguês',
                'Dinamarquês', 'Holandês', 'Finlandês', 'Polonês', 'Eslovaco', 'Esloveno', 'Catalão', 'Galego',
                'Basco', 'Galês', 'Córnico', 'Bretão', 'Alemão', 'Inglês', 'Francês', 'Espanhol', 'Italiano',
                'Português', 'Russo', 'Chinês', 'Japonês', 'Coreano', 'Árabe', 'Turco', 'Hindi', 'Indonésio']

#contar quantos idiomas tem na lista
print(len(lista_idiomas))
#contar quantos idiomas repetidos tem na lista
print(len(lista_idiomas) - len(set(lista_idiomas)))

#criar uma lista de idiomas sem repeticao
lista_idiomas_sem_repeticao = list(set(lista_idiomas))
#contar quantos idiomas tem na lista sem repeticao
print(len(lista_idiomas_sem_repeticao))

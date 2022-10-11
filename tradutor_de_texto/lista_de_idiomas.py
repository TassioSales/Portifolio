lista_idiomas = ["French","Spanish", "Japanese", "Italian", "German", "Russian", "Portuguese", "Chinese", "Korean",
                    "Dutch", "Polish", "Swedish", "Turkish", "Greek", "Czech", "Hungarian", "Romanian", "Finnish",
                    "Norwegian", "Danish", "Arabic", "Hebrew", "Hindi", "Thai", "Vietnamese", "Indonesian", "Malay",
                    "Bengali", "Persian", "Urdu", "Tamil", "Telugu", "Kannada", "Malayalam", "Sinhala", "Burmese",
                    "Khmer", "Lao", "Georgian", "Mongolian", "Amharic", "Gujarati", "Punjabi", "Oriya", "Marathi",
                    "Sanskrit", "Hausa", "Yoruba", "Igbo", "Swahili", "Zulu", "Xhosa", "Malagasy", "Maltese",
                    "Icelandic", "Albanian", "Serbian", "Croatian", "Bosnian", "Macedonian", "Slovenian", "Bulgarian",
                    "Estonian", "Latvian", "Lithuanian", "Afrikaans", "Tagalog", "Haitian", "Cebuano", "Esperanto",
                    "Welsh", "Basque", "Catalan", "Galician", "Scottish Gaelic", "Irish", "Manx", "Cornish", "Breton",
                    "Akan", "Twi", "Fula", "Hausa", "Yoruba", "Igbo", "Swahili", "Zulu", "Xhosa", "Malagasy", "Maltese",
                    "Icelandic", "Albanian", "Serbian", "Croatian", "Bosnian", "Macedonian", "Slovenian", "Bulgarian",
                    "English", "Estonian", "Latvian", "Lithuanian", "Afrikaans", "Tagalog", "Haitian", "Cebuano",
                    "Esperanto", "Welsh", "Basque", "Catalan", "Galician", "Scottish Gaelic", "Irish", "Manx", "Cornish"]

#contar quantos idiomas tem na lista
print(len(lista_idiomas))
#contar quantos idiomas repetidos tem na lista
print(len(lista_idiomas) - len(set(lista_idiomas)))
#criar lista de idiomas sem repetiçoes
lista_idiomas_ordenada = sorted(set(lista_idiomas))
#contar quantos idiomas tem na lista sem repetiçoes
print(len(lista_idiomas_ordenada))



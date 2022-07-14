import whois

site = ("udemy.com")
dados = whois.query(site)

print(f'''
    Dominio: {dados.name}
    pais de registro: {dados.registrant_country}
    Abertura do registro: {dados.creation_date}
    Status de servidor: {dados.status}
''')
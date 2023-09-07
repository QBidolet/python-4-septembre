import cgitb

cgitb.enable()

print('Content-type: text/html')

nom = "Quentin"

print(
    """
    <html>
    <head>
    <title>Exemple CGI</title>
    </head>
    <body>
    <h1>Exemple CGI</h1>
    <p>Mon nom est {nom}</p>
    </body>
    </html>
    """
      )


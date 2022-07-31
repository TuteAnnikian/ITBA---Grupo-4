import html 

def create_report(table,client,fname):
  template= f"""<!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link rel = "stylesheet" href="main.css" />
      <title>Reporte</title>
  </head>
  <body>
    <div id="cliente"> 
      {client}
    </div>
    <div id ="transaccion"> 
      {table}
    </div>
  </body>
  </html>"""

  f = open(f"{fname}.html", "w", encoding='utf-8')
  f.write(template)  
  f.close









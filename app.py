from flask import Flask, render_template_string, request

app = Flask(__name__)

# Función que convierte dólares a euros con una tasa fija
def dolares_a_euros(dolares: float) -> float:
    return round(dolares * 0.85, 2)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Global Exchange</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>

        body{
            background: linear-gradient(135deg,#0f172a,#1e3a8a);
            min-height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
            font-family:'Segoe UI',sans-serif;
        }

        .card{
            width:520px;
            max-width:95%;
            border:none;
            border-radius:20px;
            box-shadow:0 20px 45px rgba(0,0,0,.35);
            padding:40px;
        }

        .logo{
            font-size:60px;
        }

        h1{
            color:#1E40AF;
            font-weight:bold;
        }

        .btn-custom{
            background:#2563EB;
            color:white;
            width:100%;
            border-radius:10px;
            padding:12px;
            font-size:18px;
            font-weight:bold;
        }

        .btn-custom:hover{
            background:#1D4ED8;
            color:white;
        }

        .resultado{
            margin-top:25px;
            background:#dcfce7;
            border-left:6px solid #16a34a;
            padding:20px;
            border-radius:10px;
        }

        footer{
            margin-top:20px;
            font-size:13px;
            color:gray;
        }

    </style>

</head>

<body>

<div class="card">

<div class="text-center">

<div class="logo">💱</div>

<h1>Global Exchange</h1>

<p class="text-muted">
Conversor profesional de dólares estadounidenses a euros.
</p>

</div>

<form method="POST">

<div class="mb-3">

<label class="form-label fw-bold">
Monto en dólares (USD)
</label>

<input
type="number"
step="any"
name="dolares"
class="form-control form-control-lg"
placeholder="Ejemplo: 150"
required
value="{{ dolares }}">

</div>

<button class="btn btn-custom">

Convertir Divisa

</button>

</form>

{% if resultado is not none %}

<div class="resultado">

<h5 class="text-success">

✔ Conversión realizada correctamente

</h5>

<hr>

<p>

<strong>Monto ingresado:</strong>

{{ dolares }} USD

</p>

<p>

<strong>Tasa aplicada:</strong>

1 USD = 0.85 EUR

</p>

<h4 class="text-primary">

{{ resultado }} EUR

</h4>

</div>

{% endif %}

<footer class="text-center">

© 2026 Global Exchange

</footer>

</div>

</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def home():

    resultado=None
    dolares=""

    if request.method=="POST":

        try:

            dolares=request.form.get("dolares","")

            resultado=dolares_a_euros(float(dolares))

        except ValueError:

            resultado="Valor inválido"

    return render_template_string(
        HTML_TEMPLATE,
        resultado=resultado,
        dolares=dolares
    )

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
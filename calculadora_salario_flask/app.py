from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    try:
        salario = float(request.form['salario'])
        dependentes = int(request.form['dependentes'])
    except ValueError:
        return "Erro: Insira valores válidos."

    if salario < 0:
        return "Erro: O salário não pode ser negativo."

    if dependentes <= 0:
        return "Erro: O número de dependentes não pode ser negativo."

    inss = salario * 0.08

    if salario > 5000:
        ir = salario * 0.15
    else:
        ir = 0

    desconto_dependentes = dependentes * 200

    resultado = salario - inss - ir + desconto_dependentes

    return f"Salário líquido: R$ {resultado:.2f}"

if __name__ == '__main__':
    app.run(debug=True)

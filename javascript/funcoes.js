function saudacao(nome) { // nome é um parametro da função saudação
    console.log('Olá,', nome)
}

saudacao('Gabriel') // Gabriel é o argumento
saudacao('Jéssica')
saudacao('Nathalia')

function calcularDobroDeUm(numero) {
    return numero * 2
}

const numeroDobrado = calcularDobroDeUm(4)
console.log('O dobro de 4 é:', numeroDobrado)
// 1. Boas-vindas personalizadas
// Crie uma variável chamada nome e atribua seu nome completo. 
// Depois, use console.log() para exibir a mensagem: "Olá, [nome]! Seja bem-vindo(a) ao curso de JavaScript!"


let nome = 'Gabriel Torquato Alves'

console.log('Olá, ',nome,'! Seja bem-vindo ao curso de JavaScript!')

// 2. Cálculo de idade
// Crie duas variáveis: anoAtual e anoNascimento. 
// Calcule a idade da pessoa subtraindo os valores e exiba no console: "Você tem [idade] anos."

let anoAtual = 2025
let anoNascimento = 1994

let idade = anoAtual - anoNascimento

console.log('Você tem ', idade,'anos.')

// 3. Mensagem de localização
// Crie três variáveis com os dados da sua localização: cidade, estado e pais. 
// Em seguida, mostre no console: "Você está em Cidade - Estado, País."

let cidade = 'Capivari de Baixo'
let estado = 'Santa Catarina'
let pais = 'Brasil'

console.log('Você está em', cidade,'-', estado,'-', pais)

// 4. Tipo da variável:
// Crie uma variável chamada temCarteira com valor true ou false. 
// Use console.log(typeof temCarteira) para mostrar o tipo dessa variável.

let temCarteira = false

console.log(typeof temCarteira)

// 5. Simulação bancária simples:
// Crie uma variável saldo iniciando com 0. Depois, simule um depósito de 200 e um saque de 50. 
// Mostre o saldo final no console com uma frase explicando.

let saldo = 0
let deposito = 200
let saque = 50

let saldofinal = saldo + deposito - saque

console.log('Seu saldo final após depósito e saque: ', saldofinal)

// 1. Contador de 1 a 10
// Use um for para mostrar no console os números de 1 até 10, um por linha.

for (let i = 0; i <= 10; i++) {
    console.log(i)
}

// 2. Soma de 1 a 100
// Some todos os números de 1 a 100. Mostre o resultado no final com uma mensagem explicativa.

let soma = 0;

for (let i = 1; i <= 100; i++) {
    soma += i;
}

console.log("Soma de 1 a 100: " + soma);

// 3. Tabuada personalizada
// Peça um número e mostre a tabuada desse número (de 1 a 10) usando um for.

let numeroTabuada = 7;

for (let i = 1; i <= 10; i++) {
    console.log(numeroTabuada + " x " + i + " = " + (numeroTabuada * i));
}
// let videoJuego = [ 'mario 3', 'megaban', 'chrono trigger' ];
// console.log (videoJuego[1]);

// let arreglo2 = ['andrea', true, 123, 4+6,['mario 3', 'megaban', 'chrono trigger']];

// console.log(arreglo2[3])

// console.log(arreglo2[4][1]);


// agregar 
let frutas = ["manzana", "naranja", "fresa", "piña"];
frutas.push('paltano');

console.log(frutas);

// saca la ultima palabra de la lista
let ultimafruta = frutas.pop();
console.log(frutas); 
console.log(ultimafruta);

// modificar
let primerafruta = frutas .shift();
console.log(frutas);
console.log(primerafruta);

// saca la primera palabra de la lista
frutas.unshift("manzana");
console.log(frutas);

// conecta dos arreglos
let verduras =["zanahoria", "pepino"];
let cereales = ['almendras', 'mani'];
let alimentos = frutas.concat(verduras, cereales);
console.log(alimentos);

// extrae uma parte del array sin modificar el array original
let partefrutas = frutas.slice(1,3);
console.log(partefrutas);
console.log(frutas);

// remplaza una palabra del arreglo 
frutas.splice(2,1, "kiwi");
console.log(frutas);

// imprime cada elemento del arreglo con un forEach
frutas.forEach(function(fruta) {
    console.log(frutas);
});

// crea un nuevo arreglo con los elementos multiplicados por 2
let numeros = [1, 2, 3, 4];
let dobles = numeros.map(function(numero) {
    return numero * 2;
});
console.log(dobles);

// ayuda a encontrar valores con una condicion 
let encontrado = numeros.find(function(numero) {
    return numero > 2;
});
console.log(encontrado);

// ayuda a encontrar todos los valores que cumplen una condicion
let numeros2 = [1,2,8];
let algunoMayorquetres = numeros2.some(function(numero) {
    return numero > 3;
});
console.log(algunoMayorquetres);

// todos menores que 5
let todosMenoresquecinco = numeros.every(function(numero) {
    return numero < 5;
});
console.log(todosMenoresquecinco);
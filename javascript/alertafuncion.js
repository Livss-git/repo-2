let sueldo = (vent,sala)=>sala+vent*0.1;

let venta = prompt('escribir el valor de la venta: ');
let salario = prompt('escriba el salario del vendedor: ');

sueldofin=sueldo(parseInt(venta),parseInt(salario));
alert(`el sueldo es: ${sueldofin}`);
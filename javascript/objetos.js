const personaje ={
    nombre: 'tony stark',
    codename: 'iroman',
    vivo: false,
    edad: 40,
    coords: {
        lat: 34.034,
        lng: -118.70
    },
    trajes: ['mark 1', 'mark v', 'hulk buster'],
    direccion: {
        zip: '10880, 90265',
        ubicacion: 'malibu, california'
    },
    'ultima pelicula': 'infinity war'
};

console.log(personaje);
console.log('nombre', personaje.nombre);
console.log('nombre', personaje['nombre']);
console.log('edad', personaje.edad);
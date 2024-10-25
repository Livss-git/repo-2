const personaje = {
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
    'Ultima pelicula': 'infinity war'
};

console.log(personaje);
console.log('nombre', personaje.nombre);
console.log('nombre', personaje['nombre']);
console.log('edad', personaje.edad);

console.log('coords', personaje.coords);
console.log('lat', personaje.coords.lat);

console.log('No. trajes', personaje.trajes.length );
console.log('ultimo traje', personaje.trajes[ personaje.trajes.length - 1 ]);

const x = 'vivo';
console.log('vivo', personaje[x]);

console.log('Ultima pelicula', personaje['ultima-pelicula']);
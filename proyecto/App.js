import React, { useState } from 'react';
import './App.css';

function App() {
  // Estado para almacenar los materiales y la búsqueda
  const [materiales, setMateriales] = useState([]);
  const [nombre, setNombre] = useState('');
  const [descripcion, setDescripcion] = useState('');
  const [busqueda, setBusqueda] = useState('');

  // Función para registrar material
  const registrarMaterial = () => {
    if (nombre && descripcion) {
      const nuevoMaterial = { nombre, descripcion };
      setMateriales([...materiales, nuevoMaterial]);
      setNombre('');
      setDescripcion('');
    } else {
      alert('Por favor, ingresa un nombre y una descripción para el material.');
    }
  };

  // Función para manejar el cambio en el campo de búsqueda
  const manejarBusqueda = (evento) => {
    setBusqueda(evento.target.value);
  };

  // Filtrar los materiales según la búsqueda
  const materialesFiltrados = materiales.filter((material) =>
    material.nombre.toLowerCase().includes(busqueda.toLowerCase())
  );

  return (
    <div className="container">
      <h1>Gestión de Materiales</h1>

      {/* Formulario de registro */}
      <div className="form-container">
        <h2>Registrar Material</h2>
        <input
          type="text"
          value={nombre}
          onChange={(e) => setNombre(e.target.value)}
          placeholder="Nombre del material"
        />
        <input
          type="text"
          value={descripcion}
          onChange={(e) => setDescripcion(e.target.value)}
          placeholder="Descripción del material"
        />
        <button onClick={registrarMaterial}>Registrar</button>
      </div>

      {/* Buscador */}
      <div className="search-container">
        <h2>Buscar Material</h2>
        <input
          type="text"
          value={busqueda}
          onChange={manejarBusqueda}
          placeholder="Buscar por nombre..."
        />
      </div>

      {/* Lista de materiales */}
      <div className="materials-container">
        <h2>Materiales Registrados</h2>
        <ul id="material-list">
          {materialesFiltrados.length === 0 ? (
            <li>No hay materiales registrados.</li>
          ) : (
            materialesFiltrados.map((material, index) => (
              <li key={index}>
                <strong>{material.nombre}</strong>: {material.descripcion}
              </li>
            ))
          )}
        </ul>
      </div>
    </div>
  );
}

export default App;
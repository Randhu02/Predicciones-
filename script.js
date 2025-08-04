document.addEventListener('DOMContentLoaded', () => {
  const version = document.getElementById('version');
  const producto = document.getElementById('producto');
  const area = document.getElementById('area');

  // Puedes cargar datos dinámicamente aquí más adelante
  version.addEventListener('change', () => {
    console.log("Versión seleccionada:", version.value);
  });

  producto.addEventListener('change', () => {
    console.log("Producto seleccionado:", producto.value);
  });

  area.addEventListener('change', () => {
    console.log("Área seleccionada:", area.value);
  });
});

var data = "{{ data|safe }}";
console.log(data)

document.addEventListener('DOMContentLoaded', function () {
    fetch('http://127.0.0.1:8000/appEntrega/productos/')
    .then(response => response.json())
    .then(data => console.log(data));
});

const tablaProductos = document.querySelector('#tablaProductos');


function generateCodigo(data) {
    console.log(data)
    for (i = 0; i < data.length; i++) {
        console.log(data)
    }
}
const tablaProductos = document.querySelector('#tablaProductos');
const tablaProductosBody = tablaProductos.childNodes[3];
let datosProductos = '';


document.addEventListener('DOMContentLoaded', function () {

    fetch('http://127.0.0.1:8000/appEntrega/productos-json/', {
        headers: {
            'Accept': 'application/json',
        },
    })
        .then(response => response.json())
        .then(data => datosProductos = data)
        .then(() => datosProductos.length > 0 ? generarCodigoProductos() : generarCodigoVacio());
});


function generarCodigoProductos() {

    datosProductos.forEach(pro => {
        let tr = document.createElement('TR')

        tr.addEventListener('dblclick', () => {
            document.location.href = `http://127.0.0.1:8000/appEntrega/productos/${pro.producto_referencia}/editar`;
        })

        let tdCodigo = document.createElement('TD')
        tdCodigo.textContent = pro.producto_referencia
        tr.appendChild(tdCodigo);

        let tdProducto = document.createElement('TD')
        tdProducto.textContent = pro.producto_nombre
        tr.appendChild(tdProducto);

        let tdDescripcion = document.createElement('TD')
        tdDescripcion.textContent = pro.producto_descripcion
        tr.appendChild(tdDescripcion);

        let tdCategoria = document.createElement('TD')
        tdCategoria.textContent = pro.producto_categoria
        tr.appendChild(tdCategoria);

        let tdPtrecio = document.createElement('TD')
        tdPtrecio.textContent = pro.producto_precio
        tr.appendChild(tdPtrecio);

        tablaProductosBody.appendChild(tr)
    });
}

function generarCodigoVacio() { 
    let tr = document.createElement('TR')
    let td = document.createElement('TD')

    td.colSpan = "5"
    td.textContent = "No existen productos"

    tr.appendChild(td);
    tablaProductosBody.appendChild(tr)
}

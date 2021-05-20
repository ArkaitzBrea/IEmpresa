const tablaProductos = document.querySelector('#tablaProductos');
const tablaProductosBody = tablaProductos.childNodes[3];

let datosProductos = '';

const orderUp = document.getElementById('orderUp')
const orderDown = document.getElementById('orderDown')
const opcionesOrdenar = document.getElementById('opcionesOrdenar');

orderUp.addEventListener('click', () => {

    orderUp.classList.remove('c-grey')
    orderDown.classList.add('c-grey')
    ordenar();
})

orderDown.addEventListener('click', () => {

    orderDown.classList.remove('c-grey')
    orderUp.classList.add('c-grey')
    ordenar();
})

opcionesOrdenar.addEventListener('change', (e) => {
    localStorage.setItem("metodoOrdenar", e.target.value);
    ordenar();
})



document.addEventListener('DOMContentLoaded', function () {

    localStorage.setItem("metodoOrdenar", "producto_precio")

    fetch('http://127.0.0.1:8000/appEntrega/productos-json/', {
        headers: {
            'Accept': 'application/json',
        },
    })
        .then(response => response.json())
        .then(data => datosProductos = data)
        .then(() => { ordenar() })
        //.then(() => datosProductos.length > 0 ? generarCodigoProductos() : generarCodigoVacio());
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

function ordenar() {
    let metodoOrdenar = localStorage.getItem("metodoOrdenar")

    if (orderUp.classList.contains('c-grey')) {
        datosProductos.sort((a, b) =>
            a.producto_precio > b.producto_precio ? 1 : -1
        )
    } else {
        datosProductos.sort((a, b) =>
            b.producto_precio > a.producto_precio ? 1 : -1
        );
    }

    tablaProductosBody.childNodes.forEach(child => {
        tablaProductosBody.removeChild(child)
    })

    generarCodigoProductos();
}

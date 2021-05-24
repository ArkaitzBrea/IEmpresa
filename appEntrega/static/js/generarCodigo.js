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
        .then(() => datosProductos.length > 0 ? ordenar() : generarCodigoVacio());
});


function generarCodigoProductos() {
    tablaProductos.appendChild(tablaProductosBody);
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
        

        let tdArchivo = document.createElement('TD')
        let aArchivo = document.createElement('A')
        aArchivo.setAttribute('download', '')
        aArchivo.href = `http://127.0.0.1:8000/media/${pro.producto_pdf}/`
 

        aArchivo.innerHTML = '<i class="fas fa-download"></i>';

        tdArchivo.appendChild(aArchivo);
        tr.appendChild(tdArchivo);
        tablaProductosBody.appendChild(tr);
    });
}

function generarCodigoVacio() {
    let tr = document.createElement('TR')
    let td = document.createElement('TD')

    td.colSpan = "7"
    td.textContent = "No existen productos"

    tr.appendChild(td);
    tablaProductosBody.appendChild(tr)
}

function ordenar() {
    let metodoOrdenar = localStorage.getItem("metodoOrdenar")

    if (orderUp.classList.contains('c-grey')) {
        ordenarAscendente(metodoOrdenar);

    } else {
        ordenarDescendente(metodoOrdenar);
    }
    if (tablaProductosBody.childNodes.length > 1) {
        for (let i = 0; i <= datosProductos.length; i++) {
            if (tablaProductosBody.hasChildNodes()) {
                tablaProductosBody.removeChild(tablaProductosBody.firstChild)
            }
        }
    }
    generarCodigoProductos();
}

function ordenarAscendente(metodoOrdenar) {
    if (metodoOrdenar == "producto_referencia") {
        datosProductos.sort((a, b) =>
            a.producto_referencia > b.producto_referencia ? 1 : -1)
    } else if (metodoOrdenar == "producto_nombre") {
        datosProductos.sort((a, b) =>
            a.producto_nombre > b.producto_nombre ? 1 : -1)
    } else if (metodoOrdenar == "producto_descripcion") {
        datosProductos.sort((a, b) =>
            a.producto_descripcion > b.producto_descripcion ? 1 : -1)
    } else if (metodoOrdenar == "producto_categoria") {
        datosProductos.sort((a, b) =>
            a.producto_categoria > b.producto_categoria ? 1 : -1)
    } else if (metodoOrdenar == "producto_precio") {
        datosProductos.sort((a, b) =>
            a.producto_precio > b.producto_precio ? 1 : -1)
    }
}

function ordenarDescendente(metodoOrdenar) {
    if (metodoOrdenar == "producto_referencia") {
        datosProductos.sort((b, a) =>
            a.producto_referencia > b.producto_referencia ? 1 : -1)
    } else if (metodoOrdenar == "producto_nombre") {
        datosProductos.sort((b, a) =>
            a.producto_nombre > b.producto_nombre ? 1 : -1)
    } else if (metodoOrdenar == "producto_descripcion") {
        datosProductos.sort((b, a) =>
            a.producto_descripcion > b.producto_descripcion ? 1 : -1)
    } else if (metodoOrdenar == "producto_categoria") {
        datosProductos.sort((b, a) =>
            a.producto_categoria > b.producto_categoria ? 1 : -1)
    } else if (metodoOrdenar == "producto_precio") {
        datosProductos.sort((b, a) =>
            a.producto_precio > b.producto_precio ? 1 : -1)
    }
}

const expresiones = {
    text: /^[a-zA-Z0-9\s]{1,250}$/, // Letras, numeros, espacios
    mail: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
    number: /^\d{1,14}$/ // 7 a 14 numeros.
}

const formulario = document.getElementById('formulario');

let formulario__grupo = "";
let formulario__p = "";
let formulario__i = "";
let cerrarAlertaEstado = 0;

let campos = {
    name: false,
    apellidos: false,
    correo: false,
    id_producto_referencia: false,
    contrasenya: false,
    contrasenya2: false
}

document.addEventListener('DOMContentLoaded', function () {
    estadoFormulario();
});

function estadoFormulario() {

    const inputs = document.querySelectorAll('.formulario__grupo-input input');

    inputs.forEach(input => {

        input.onfocus = () => {

            formulario__grupo = input.parentElement.parentElement.parentElement.parentElement;
            formulario__p = input.parentElement.parentElement.parentElement.parentElement.lastChild.previousSibling;
            formulario__i = input.nextElementSibling;

            fijarContenidoFocus(formulario__grupo, formulario__i);
        }
        input.onblur = () => {
            if (input.value.trim().length === 0) {

                borrarContenido(formulario__grupo, formulario__i, input.id);

            } else {
                validarTextos(input);
            }
        }
    });
}

function validarTextos(input) {
    debugger;
    const type = input.type;
    const value = input.value;

    if (expresiones[type].test(value))
        mensajeCorrecto(formulario__grupo, formulario__p, formulario__i, input.type);
    else
        mensajeIncorrecto(formulario__grupo, formulario__p, formulario__i, input.type);
}


function mensajeCorrecto(formulario__grupo, formulario__p, formulario__i, inputId) {
    formulario__grupo.classList.remove('wrong', 'question');
    formulario__grupo.classList.add('fixed');
    formulario__p.classList.remove('mostrar');
    formulario__i.classList.remove('fa-times-circle', 'fa-question-circle', 'warning');
    formulario__i.classList.add('fa-check-circle', 'correct');

    campos[inputId] = true;
}

function mensajeIncorrecto(formulario__grupo, formulario__p, formulario__i, inputId) {
    formulario__grupo.classList.remove('question');
    formulario__grupo.classList.add('wrong');
    formulario__p.classList.add('mostrar');
    formulario__i.classList.remove('fa-check-circle', 'correct', 'warning');
    formulario__i.classList.add('fa-times-circle');

    campos[inputId] = false;
}

function borrarContenido(formulario__grupo, formulario__i, inputId) {
    formulario__grupo.classList.remove('fixed');
    formulario__grupo.classList.remove('focus');
    formulario__i.classList.remove('fa-times-circle', 'fa-check-circle', 'fa-question-circle', 'correct');
    formulario__grupo.lastChild.previousSibling.classList.remove('mostrar');

    campos[inputId] = false;
}

function fijarContenidoFocus(formulario__grupo, formulario__i) {
    formulario__grupo.classList.remove('fixed', 'wrong');
    formulario__i.classList.remove('fa-times-circle', 'fa-check-circle');
    formulario__grupo.classList.add('focus');
}
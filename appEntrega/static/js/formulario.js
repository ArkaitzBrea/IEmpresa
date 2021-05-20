const expresiones = {
    text: /^.{1,250}$/, // Letras, numeros, espacios
    email: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
    number: /^[0-9.,]{1,14}$/
}

const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('.formulario__grupo-input input');

let formulario__grupo = "";
let formulario__p = "";
let formulario__i = "";
let cerrarAlertaEstado = 0;

document.addEventListener('DOMContentLoaded', function () {
    estadoFormulario();
});

function estadoFormulario() {
    inputs.forEach(input => {

        input.onfocus = () => {
            formulario__grupo = input.parentElement.parentElement.parentElement.parentElement;
            formulario__p = input.parentElement.parentElement.parentElement.parentElement.lastChild.previousSibling;
            formulario__i = input.nextElementSibling;

            fijarContenidoFocus(formulario__grupo, formulario__i);
        }
        input.onblur = () => {
            debugger;
            if (input.value.trim().length === 0) {
                borrarContenido(formulario__grupo, formulario__i);

            } else {
                validarTextos(input);
            }
        }
    });
}

function validarTextos(input) {
    const type = input.type;
    const value = input.value;

    if (expresiones[type].test(value))
        mensajeCorrecto(formulario__grupo, formulario__p, formulario__i);
    else
        mensajeIncorrecto(formulario__grupo, formulario__p, formulario__i);
}


function mensajeCorrecto(formulario__grupo, formulario__p, formulario__i) {
    formulario__grupo.classList.remove('wrong', 'question');
    formulario__grupo.classList.add('fixed');
    formulario__p.classList.remove('mostrar');
    formulario__i.classList.remove('fa-times-circle', 'fa-question-circle', 'warning');
    formulario__i.classList.add('fa-check-circle', 'correct');
}

function mensajeIncorrecto(formulario__grupo, formulario__p, formulario__i) {
    formulario__grupo.classList.remove('question');
    formulario__grupo.classList.add('wrong');
    formulario__p.classList.add('mostrar');
    formulario__i.classList.remove('fa-check-circle', 'correct', 'warning');
    formulario__i.classList.add('fa-times-circle');
}

function borrarContenido(formulario__grupo, formulario__i) {
    formulario__grupo.classList.remove('fixed');
    formulario__grupo.classList.remove('focus');
    formulario__i.classList.remove('fa-times-circle', 'fa-check-circle', 'fa-question-circle', 'correct');
    formulario__grupo.lastChild.previousSibling.classList.remove('mostrar');
}

function fijarContenidoFocus(formulario__grupo, formulario__i) {
    formulario__grupo.classList.remove('fixed', 'wrong');
    formulario__i.classList.remove('fa-times-circle', 'fa-check-circle');
    formulario__grupo.classList.add('focus');
}
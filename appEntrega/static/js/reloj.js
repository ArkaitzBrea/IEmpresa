const horaContainer = document.querySelector('.fecha')
date = new Date()
horaContainer.innerHTML = ` ${comp(date.getUTCDate())} / ${comp(date.getMonth() + 1)} / ${comp(date.getFullYear())} -  ${comp(date.getUTCHours() + 2)}:${comp(date.getUTCMinutes())}:${comp(date.getUTCSeconds())}`

const actualizarHora = setInterval(function () {
    date = new Date()
    horaContainer.innerHTML = ` ${comp(date.getUTCDate())} / ${comp(date.getMonth() + 1)} / ${comp(date.getFullYear())} -  ${comp(date.getUTCHours() + 2)}:${comp(date.getUTCMinutes())}:${comp(date.getUTCSeconds())}`
}, 1000)

// COMPROBAR LA LONGITUD DEL CAMPO
function comp(campo) {
    if (campo.toString().length == 1)
        return `0${campo.toString()}`
    else
        return campo.toString()
}
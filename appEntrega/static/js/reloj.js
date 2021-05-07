const horaContainer = document.querySelector('.fecha')
/* const minutosContainer = document.querySelector('.minutos')
const segundosContainer = document.querySelector('.segundos') */

const actualizarHora = setInterval(function () {
    /* let horas = date.getHours()
    let minutos = date.getMinutes()
    let segundos = date.getSeconds()
    horaContainer.innerHTML = horas
    minutosContainer.innerHTML = minutos
    segundosContainer.innerHTML = segundos */
    const date = new Date()
    //REFACTORIZADO
    horaContainer.innerHTML = ` ${date.getUTCDate()} / ${date.getUTCMonth()} / ${date.getFullYear()} -  ${date.getUTCHours()} : ${date.getUTCMinutes()}`

}, 1000)
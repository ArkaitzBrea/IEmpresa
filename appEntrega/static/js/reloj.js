const horaContainer = document.querySelector('.fecha')

const actualizarHora = setInterval(function () {
    const date = new Date()
    horaContainer.innerHTML = ` ${date.getUTCDate()} / ${date.getUTCMonth()} / ${date.getFullYear()} -  ${date.getUTCHours()} : ${date.getUTCMinutes()}`

}, 1000)
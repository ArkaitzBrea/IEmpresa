const horaContainer = document.querySelector('.fecha')

const actualizarHora = setInterval(function () {
    const date = new Date()
    horaContainer.innerHTML = ` ${date.getUTCDate()} / ${date.getUTCMonth() + 1} / ${date.getFullYear()} -  ${date.getUTCHours() + 2} : ${date.getUTCMinutes()}`

}, 1000)
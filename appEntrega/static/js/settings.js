// RESTAURAR ESTILOS ANTERIORES
obtenerEstilosAnteriores();

function obtenerEstilosAnteriores(){
  let fondo = localStorage.getItem("colorFondo");
  let letra = localStorage.getItem("colorLetra");
  let fuente = localStorage.getItem("fuente")
  document.body.style.backgroundColor = fondo;
  document.body.style.color = letra;
  document.documentElement.style.setProperty('--font-size', fuente)
  console.log(fondo);
  console.log(letra);
  console.log(fuente);
}

// CONTROL DE TAMAÑO DE FUENTE
const getFontSize = () =>
  parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--font-size'))

const subirFuente = element => {
  element.addEventListener('click', () => {
    let fontSize = getFontSize()
    document.documentElement.style.setProperty('--font-size', `${fontSize * 1.1}`)
    localStorage.setItem("fuente", fontSize)
  })
}

const bajarFuente = element => {
  element.addEventListener('click', () => {
    let fontSize = getFontSize()
    document.documentElement.style.setProperty('--font-size', `${fontSize * 0.9}`)
    localStorage.setItem("fuente", fontSize)
  })
}

addEventListener('keyup', e => {
  if (e.key === 'ArrowUp') document.getElementById('subirBtn').click()
  if (e.key === 'ArrowDown') document.getElementById('bajarBtn').click()
})

subirFuente(document.getElementById('subirBtn'))
bajarFuente(document.getElementById('bajarBtn'))


// -----------------------------------------------------------------------------------------
// CONTROL DE COLOR DEL FONDO
function fondoNegro() {
  document.body.style.backgroundColor = "#CDCDCD";
  document.body.style.color = "white";
  let fondo = "#CDCDCD";
  let letra = "white";
  localStorage.setItem("colorFondo", fondo);
  localStorage.setItem("colorLetra", letra);
}

function fondoBlanco() {
  document.body.style.backgroundColor = "white";
  document.body.style.color = "black";
  let fondo = "white";
  let letra = "black";
  localStorage.setItem("colorFondo", fondo);
  localStorage.setItem("colorLetra", letra);
}

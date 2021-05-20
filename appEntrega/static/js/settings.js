// CONTROL DE TAMAÑO DE FUENTE
const getFontSize = () =>
  parseFloat(getComputedStyle(document.documentElement)
    .getPropertyValue('--font-size'))

const fontUp = element => {
  element.addEventListener('click', () => {
    let fontSize = getFontSize()
    document.documentElement
      .style.setProperty('--font-size', `${fontSize * 1.1}`)
  })
}

const fontDown = element => {
  element.addEventListener('click', () => {
    let fontSize = getFontSize()
    document.documentElement
      .style.setProperty('--font-size', `${fontSize * 0.9}`)
  })
}

addEventListener('keyup', e => {
  if(e.key === 'ArrowUp') document.getElementById('font-up').click()
  if(e.key === 'ArrowDown') document.getElementById('font-down').click()
})

fontUp(document.getElementById('font-up'))
fontDown(document.getElementById('font-down'))


// -----------------------------------------------------------------------------------------
// CONTROL DE COLOR DEL FONDO
const btnNegro = document.getElementById('negroBtn');
const btnBlanco = document.getElementById('blancoBtn');


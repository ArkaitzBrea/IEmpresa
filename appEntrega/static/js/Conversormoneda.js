let euros;
comprobarMoneda();

function comprobarMoneda(){
    if (euros == true) {
        eurosDolares(valNum);
    } else {
        dolaresEuros(valNum)
    }
}



function eurosDolares(valNum) {
    document.getElementById("LINEA_PRECI").value=valNum*1.156236 ;
    euros = false;
  }
  function dolaresEuros(valNum) {
    document.getElementById("inputEuros").value=valNum*0.864875337; 
    euros = true;
  }

  
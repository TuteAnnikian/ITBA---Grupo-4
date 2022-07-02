const obj = [{"casa":{"compra":"121,96","venta":"127,96","agencia":"349","nombre":"Dolar Oficial","variacion":"0,27","ventaCero":"TRUE","decimales":"2"}},
{"casa":{"compra":"216,00","venta":"219,00","agencia":"310","nombre":"Dolar Blue","variacion":"-2,23","ventaCero":"TRUE","decimales":"2"}},
{"casa":{"compra":"No Cotiza","venta":"0","agencia":"311","nombre":"Dolar Soja","variacion":"0","ventaCero":"TRUE","decimales":"3"}},
{"casa":{"compra":"237,79","venta":"238,14","agencia":"312","nombre":"Dolar Contado con Liqui","variacion":"-0,41","ventaCero":"TRUE","decimales":"2"}},
{"casa":{"compra":"229,450","venta":"229,080","agencia":"313","nombre":"Dolar Bolsa","variacion":"-1,500","ventaCero":"TRUE","decimales":"3"}},
{"casa":{"compra":"9.852,070","venta":"0","agencia":"399","nombre":"Bitcoin","variacion":"-100,00","ventaCero":"TRUE","decimales":"3"}},
{"casa":{"nombre":"Dolar turista","compra":"No Cotiza","venta":"211,13","agencia":"406","variacion":"0,27","ventaCero":"TRUE","decimales":"2"}},
{"casa":{"compra":"120,37","venta":"128,25","agencia":"302","nombre":"Dolar","decimales":"3"}},
{"casa":{"nombre":"Argentina","compra":"2.121,00","venta":"-0,24","mejor_compra":"True","mejor_venta":"False","fecha":"05\/05\/15","recorrido":"16:30","afluencia":{},"agencia":"141","observaciones":{}}}]


/* la api devuelve una lista con objetos. */
/* esto se puede poner en un bucle e ir creando los elementos por cada obj de la lista
 
/* no estamos conformes con la apariencia y funcionamiento actual de la pagina, pero no queremos entregar fuera de termino*/ 


function traer(){    /* el resto de las funciones se ejecutan dentro de esta */
    console.log("se ejecuta funcion traer")
    fetch("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
    .then(res => res.json())
    .then(data =>{
        console.log((data));
       /*  console.log("iterando objeto, creando cards...");
        crearCards(data); */
        console.log("printing data...");
        printData(data);
           
    });
}


function printData(data){
    console.log("empieza a iterar printData");
    for(let n = 1; n < 7; n++){

        console.log("iteracion: "+n);

        var tipo = document.getElementById("tipo"+n);
        var compra = document.getElementById("compra"+n);
        var venta = document.getElementById("venta"+n);
        var foot = document.getElementById("foot"+n);
        var variacion = document.getElementById("var"+n);

        console.log(tipo,compra,venta,foot,variacion);
    
        var signo = ((parseFloat((data[n-1].casa.variacion).replace(',', '.'))) > 0 ? "+":"");
        var today = new Date();
        var fecha = today.getDate()+"/"+today.getMonth()+"/"+today.getFullYear()+" "+today.getHours()+":"+today.getMinutes();
    
        tipo.innerText = data[n-1].casa.nombre;
        compra.innerText = data[n-1].casa.compra;  //si valor compra /venta no cotiza , que no se muestre//
        venta.innerText = data[n-1].casa.venta;
        variacion.textContent = `Variación: ${( signo + data[n-1].casa.variacion +"%")}`
        foot.textContent = `Actualizado: ${fecha}`
    }
}

/* function crearCards(data){    como creo una card lista, por cada elemento del objeto? 
    console.log("empieza crearCards")
    for(let fila of data){
        console.log(fila);
        let x = document.createElement("div")
        x.innerHTML="hola"
        document.getElementById("insertDolares").appendChild(x)
    } */
    /* console.log("printing data...");
    printData(data); 
}*/

traer();





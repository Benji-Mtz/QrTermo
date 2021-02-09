$(document).ready(function () {
    
    const source = new EventSource("/print-data");

    source.onmessage = function (event) {
        const data = JSON.parse(event.data);

        const { num_emp, nombre, imagen, temperatura, fecha, hora, bandera, filas } = data;               

        const pathImg = imagen;

        $('.num_emp').text(num_emp);
        $('.nombre').text(nombre);
        $('.temperatura').text(temperatura);
        $('.fecha').text(fecha);
        $('.hora').text(hora);
        
        $('.filas').text(filas);
        

        console.log(filas)
        //console.log(typeof(temperatura), typeof(hora))
        //console.log(typeof(data.temperatura), typeof(data.hora), typeof(data.bandera));

        if ( temperatura < 35) {
            $("body").addClass("baja");
            $( "body" ).removeClass( "alta default blink-bg" );
        }
        else if (temperatura >= 35 && temperatura < 37) {
            $("body").addClass("default");
            $( "body").removeClass( "baja alta blink-bg" );
        } else if ( temperatura >=37 )  {
        
            $("body").addClass("blink-bg");
            $( "body").removeClass( "baja default" );

        }

        if (bandera == false) {
            $('.card-img-top').attr('src','static/img/sinperfil.png');
        } else {
            $('.card-img-top').attr('src', 'static/img/'+pathImg);
        }

    }
});
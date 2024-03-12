$(document).ready(function () {
    var table_ventas = document.getElementById('resultadoTabla');
    table_ventas.style.visibility = 'hidden';
});

$('#filtrarBtn').click(function () {
    const filterday = $('#filterday_get').val();
    const filtermonth = $("#filtermonth_get").val();
    const filteranio = $('#filteranio_get').val();
    var data = {
        filterday: filterday,
        filtermonth: filtermonth,
        filteranio: filteranio
    };

    $.ajax({
        type: "POST",
        url: "/filtrar",
        headers: {
            "X-CSRFToken": $("#csrf_token").val(),
        },
        data: data,
        beforeSend: function () {
            Swal.fire({
                title: "Consultando información",
                html: "Por favor espere...",
                allowOutsideClick: false,
                showConfirmButton: false,
                onBeforeOpen: () => {
                    Swal.showLoading();
                },
            });
        },
        success: function (response) {
            console.log(response.resultados)
            Swal.close();
            $('#resultadoTabla tbody').empty();
            var table_ventas = document.getElementById('resultadoTabla');
            table_ventas.style.visibility = 'visible';
            let suma = 0;

            response.resultados.forEach(function (resultado) {
                suma += resultado.pagoTotal;

                $('#resultadoTabla tbody').append(
                    '<tr>' +
                    '<td>' + resultado.nombreC + '</td>' +
                    '<td>$ ' + resultado.pagoTotal + '.00 MXN</td>' +
                    '</tr>'
                );
            });

            $("#resultadoTabla tfoot").append(
                '<tr>' +
                '<td>Total de venta</td>' +
                '<td>$ ' + suma + '.00 MXN</td>' +
                '</tr>'
            );
        },
        error: function (error) {
            console.error("Error en la solicitud:", error);
        }
    });
});

$("#btnVenta").on("click", function () {
    var data_table = [];

    $('#ordenes tbody tr').each(function () {
        const subtotal = $(this).find('td:eq(3)').text();
        const id = $(this).find('td:eq(4)').text();
        const nombre = $(this).find('td:eq(5)').text();
        const dia = $(this).find('td:eq(6)').text();
        const mes = $(this).find('td:eq(7)').text();
        const anio = $(this).find('td:eq(8)').text();

        var data2 = {
            subtotal: subtotal,
            id: id,
            nombre: nombre,
            dia: dia,
            mes: mes,
            anio: anio
        };

        data_table.push(data2);
    });

    Swal.fire({
        title: "Confirmación de venta",
        showDenyButton: true,
        showCancelButton: false,
        confirmButtonText: "Vender",
        denyButtonText: `Cancelar`,
        confirmButtonColor: "#57b84c",
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.close();

            $.ajax({
                headers: {
                    "X-CSRFToken": $("#csrf_token").val(),
                },
                contentType: "application/json",
                type: "POST",
                url: "/venta",
                data: JSON.stringify(data_table),
                beforeSend: function () {
                    Swal.fire({
                        title: "Realizando venta",
                        html: "Por favor espere...",
                        allowOutsideClick: false,
                        onBeforeOpen: () => {
                            Swal.showLoading();
                        },
                    });
                },
                success: function (response) {
                    Swal.fire({
                        title: "Venta realizada",
                        icon: "success",
                        showConfirmButton: false,
                        timer: 1500,
                    }).then(() => {
                        location.reload();
                    });
                },
                error: function (error) {
                    Swal.fire("Error al realizar la venta", "", "error");
                }
            });
        }
    });
});


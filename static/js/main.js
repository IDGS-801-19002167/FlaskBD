$(document).ready(function () {
    var table_ventas = document.getElementById('resultadoTabla');
    table_ventas.style.visibility = 'hidden';

    document.getElementById('clearfilter').style.display = "none";
});

$('#filtrarBtn').click(function () {
    var data = {
        filterday: $("#filterday_get").val(),
        filtermonth: $("#filtermonth_get").val(),
        filteranio: $("#filteranio_get").val(),
        filtercustomer: $("#filtercustomer").val()
    }

    document.getElementById('clearfilter').style.display = "block";

    $.ajax({
        type: "POST",
        url: "/filtrar",
        headers: {
            "X-CSRFToken": $("#csrf_token").val(),
        },
        contentType: "application/json",
        data: JSON.stringify(data),
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
            Swal.close();

            $('#resultadoTabla tbody').empty();
            var table_ventas = document.getElementById('resultadoTabla');
            table_ventas.style.visibility = 'visible';
            let suma = 0;
            console.log(response.resultados);
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

            document.getElementById('filterday_get').style.visibility = 'hidden';
            document.getElementById('filtermonth_get').style.visibility = 'hidden';
            document.getElementById('filteranio_get').style.visibility = 'hidden';
            document.getElementById('filtercustomer').style.visibility = 'hidden';
        },
        error: function (error) {
            console.error("Error en la solicitud:", error);
        }
    });

    document.getElementById('filtrarBtn').style.display = 'none';
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

$("#profile-tab").on('shown.bs.tab', function () {
    $("#ordenes tfoot").empty();
    
    $.ajax({
        headers: {
            "X-CSRFToken": $("#csrf_token").val(),
        },
        contentType: "application/json",
        type: "GET",
        url: "/orders",
        success: function (response) {
            $('#ordenes tbody').empty();
            var table_orders = document.getElementById('ordenes');
            console.log(response);

            if (response.length != 0) {
                let suma = 0;

                response.forEach(function (resultado) {
                    suma += resultado.precio;

                    $('#ordenes tbody').append(
                        '<tr>' +
                        '<td>' + resultado.tamanio + '</td>' +
                        '<td>' + resultado.ingredientes + '</td>' +
                        '<td>' + resultado.cantidad + '</td>' +
                        '<td>' + resultado.precio + '</td>' +
                        '<td hidden>' + resultado.id + '</td>' +
                        '<td hidden>' + resultado.nombre + '</td>' +
                        '<td hidden>' + resultado.dia + '</td>' +
                        '<td hidden>' + resultado.mes + '</td>' +
                        '<td hidden>' + resultado.anio + '</td>' +
                        '<td class="d-flex align-content-center flex-wrap">' +
                        '<button type="submit" class="btn btn-danger" id="itemdelete" onclick="itemDelete(' + resultado.id + ')">' +
                        '<i class="fa-solid fa-trash me-auto mx-0"></i>' +
                        '</button>&nbsp;' +
                        '<a style="text-decoration: none; color: #fff" href="itemedit?id=' + resultado.id + '">' +
                        '<button type="button" class="btn btn-info" data-bs-toggle="modal" data-bs-target="#modal_edit">' +
                        '<i class="fa-solid fa-pen-to-square me-auto mx-0"></i>' +
                        '</button>' +
                        '</a>' +
                        '</td>' +
                        '</tr>'
                    );
                });

                $("#ordenes tfoot").append(
                    '<tr>' +
                    '<td colspan="3">Total de la lista</td>' +
                    '<td colspan="2">$ ' + suma + '.00 MXN</td>' +
                    '</tr>'
                );
            } else {
                $('#ordenes tbody').append(
                    '<tr>' +
                    '<td class="text-center" colspan="5">No hay pizzas agregadas a la lista</td>' +
                    '</tr>'
                );
            }

            table_orders.style.visibility = 'visible';
        }
    })
});

$("#cleanfields").on('click', function () {
    $("#name_customer").val('');
    $("#addres_customer").val('');
    $("#phone_customer").val('');
    $("#count_pizza").val('');
    $("#year").val('');
});

$("#clearfilter").on('click', function () {
    document.getElementById('clearfilter').style.display = "none";
    document.getElementById('filtrarBtn').style.display = 'block';
    var table_ventas = document.getElementById('resultadoTabla');
    table_ventas.style.visibility = 'hidden';
    $('#resultadoTabla tbody').empty();
    $('#resultadoTabla tfoot').empty();
    $("#filteranio_get").val('');
    $("#filtermonth_get").val('');
    $("#filterday_get").val('');
    $("#filtercustomer").val('');
    document.getElementById('filterday_get').style.visibility = 'visible';
    document.getElementById('filtermonth_get').style.visibility = 'visible';
    document.getElementById('filteranio_get').style.visibility = 'visible';
    document.getElementById('filtercustomer').style.visibility = 'visible';
});

function itemDelete(id) {
    const data = {
        id: id,
    }

    $.ajax({
        url: "/deleteitem",
        headers: {
            "X-CSRFToken": $("#csrf_token").val(),
        },
        contentType: "application/json",
        type: "POST",
        data: JSON.stringify(data),
        success: function (response) {
            Swal.fire({
                title: "Pizza eliminada",
                icon: "success",
                showConfirmButton: false,
                timer: 1500,
            }).then(() => {
                location.reload();
            });
        },
        error: function (error) {
            Swal.fire("Error al eliminar la pizza", "", "error");
        }
    });
}

function additem() {
    const ingredientes = {
        jamon: $("#jamon").is(":checked"),
        pinia: $("#pinia").is(":checked"),
        champ: $("#champ").is(":checked")
    }

    const data = {
        nombre: $("#name_customer").val(),
        direccion: $("#addres_customer").val(),
        telefono: $("#phone_customer").val(),
        cantidad: $("#count_pizza").val(),
        tamanio: $("[name='tamanio']:checked").val(),
        ingredientes: ingredientes,
        fecha: $("#fecha").val(),
        anio: $("#fecha").val().split('-')[0],
    }

    $.ajax({
        url: "/pizza",
        headers: {
            "X-CSRFToken": $("#csrf_token").val(),
        },
        contentType: "application/json",
        type: "POST",
        data: JSON.stringify(data),
        success: function (response) {
            console.log(response.message);
            Swal.fire({
                title: "Pizza agregada",
                icon: "success",
                showConfirmButton: false,
                timer: 1500,
            }).then(() => {
                $("#jamon").prop("checked", false);
                $("#pinia").prop("checked", false);
                $("#champ").prop("checked", false);
                $("[name='tamanio']").prop("checked", false);
                $("#filterday").val('');
                $("#filtermonth").val('');
                $("#filteranio").val('');
                $("#count_pizza").val('');

                Swal.close();
            });
        },
        error: function (error) {
            Swal.fire("Error al agregar la pizza", "", "error");
        }
    });
}
$(document).ready(function () { $("#datatable").DataTable(), $("#datatable-buttons").DataTable(
    {  
        initComplete: function () {
            this.api().columns([0,1]).every( function (d) {
                var column = this;
                var theadname = $('#datatable-buttons th').eq([d]).text();
                var select = $('<select class="col-md-4 ml-2"><option value="">All '+theadname+'</option></select>')
                    .appendTo( '#filtertable' )
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );
                column.data().unique().sort().each( function ( d, j ) {
                    var val = $('<div/>').html(d).text();
                    select.append( '<option value="'+val+'">'+val+'</option>' )
                } );
            } );
        },
 
        "footerCallback": function ( row, data, start, end, display ) {
            var api = this.api();
            var intVal = function ( i ) {
                return typeof i === 'string' ?
                    i.replace(/[\$,]/g, '')*1 :
                    typeof i === 'number' ?
                        i : 0;
            };
            api.columns('.getTotal').every(function () {
            // Total over all pages
            // total = api
            //     .column( 3 )
            //     .data()
            //     .reduce( function (a, b) {
            //         return intVal(a) + intVal(b);
            //     }, 0 );
            //     alert(total)
 
            // Total over this page
            pageTotal = api
                .column(  this.index(), { page: 'current'} )
                .data()
                .reduce( function (a, b) {
                    return intVal(a) + intVal(b);
                }, 0 );
 
            $( api.column(  this.index() ).footer() ).html(
                pageTotal 
            );
        }); 
        },
        lengthChange: !1, buttons: [] ,title: '' }).buttons().container().appendTo("#datatable-buttons_wrapper .col-md-6:eq(0)"), $(".dataTables_length select").addClass("form-select form-select-sm") });

        $(document).ready(function(){
            $("#filtertable").hide();
            
                $('#filter').click(function(){
                $("#filtertable").slideToggle();
                });   
            });
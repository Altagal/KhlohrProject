//DATATABLE
$(document).ready(function() {
			$('.all-spells-table').DataTable({
			    paging: false,
			    columnDefs: [{ orderable: false, targets: -1 }, { orderable: false, targets: 5 }],
			    info: false,

            } );
		});
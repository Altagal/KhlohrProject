//DATATABLE
$(document).ready(function() {
    $('.spells-table').DataTable({
	    paging: true,
		pageLength: 10,
		bLengthChange: false,
		columnDefs: [{ orderable: false, targets: -1 }, { orderable: false, targets: -3 }],
		info: false,
    });
});

$(document).ready(function() {
    $('.spell-school-table').DataTable({
	    paging: true,
		pageLength: 10,
		bLengthChange: false,
		columnDefs: [{ orderable: false, targets: -1 }, ],
		info: false,
		searching:true,
    });
});


$(document).ready(function() {
    $('.no-paging-table').DataTable({
	    paging: false,
		pageLength: 10,
		bLengthChange: false,
		columnDefs: [{ orderable: false, targets: -1 }],
		info: false,
    });
});

$(document).ready(function() {
    $('.generic-table').DataTable({
	    paging: true,
		pageLength: 10,
		bLengthChange: false,
		columnDefs: [{ orderable: false, targets: -1 }],
		info: false,
    });
});
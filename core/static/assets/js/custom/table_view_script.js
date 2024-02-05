//DATATABLE
$(document).ready(function() {
    $('.all-spells-table').DataTable({
	    paging: true,
		pageLength: 10,
		bLengthChange: false,
		columnDefs: [{ orderable: false, targets: -1 }, { orderable: false, targets: 5 }],
		info: false,
    });
});

$(document).ready(function() {
    $('.spells-table').DataTable({
	    paging: true,
		pageLength: 10,
		bLengthChange: false,
		columnDefs: [{ orderable: false, targets: -1 }, { orderable: false, targets: 4 }],
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
    $('.generic-table').DataTable({
	    paging: true,
		pageLength: 10,
		bLengthChange: false,
		columnDefs: [{ orderable: false, targets: -1 }],
		info: false,
    });
});
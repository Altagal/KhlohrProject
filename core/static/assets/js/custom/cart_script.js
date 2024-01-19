const print_card_button = document.getElementById("print-cards");

print_card_button.addEventListener('click', ()=>{
    window.print();
});

//DATATABLE
$(document).ready(function() {
			$('.table').DataTable({
			    paging: false,
			    columnDefs: [{ orderable: false, targets: -1 }, ],
			    ordering: true,
			    order: [[ 0, 'asc' ]],
			    searching:false,
			    info: false,
			});
});







//EM DESUSO
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

function add_card(slug, type){

    let url = "/add_card"

    let params = {
        card_slug:slug,
        card_type:type,
    }

     fetch(url, {
        method:"POST",
        headers:{
            "Content-Type" : "application/json",
            "X-CSRFToken" : csrftoken
        },
        body: JSON.stringify(params),
    })
    .then(response=>response.json())
    .catch(error=>{console.log(error)})
}
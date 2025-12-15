document.addEventListener("DOMContentLoaded", function () {

    const first_card = document.querySelector(".card:not(.no_print)");
    const first_card_html = first_card.outerHTML;
    const button_card = document.querySelector(".card.no_print");
    const button = document.getElementById("novo");

    button.addEventListener("click", function () {
        const wrapper = document.createElement("div");
        wrapper.innerHTML = first_card_html;
        const new_card = wrapper.firstElementChild;
        button_card.parentNode.insertBefore(new_card, button_card);

    });
});
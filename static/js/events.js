const hamburger_icon = document.getElementById('hamburger-icon');
const cancel_icon = document.getElementById('cancle-icon');
const menu_item = document.getElementById('mobile-menu-content');
const ticket_btn = document.getElementById('ticket-btn');
const get_ticket = document.getElementById('get-ticket');
const contact_phone = document.getElementById('contact-phone');
const contact_phone_item = document.getElementById('contact-phone-item');
const contact_email = document.getElementById('contact-email');
const contact_email_item = document.getElementById('contact-email-item');
const cart_page = document.getElementById('cart-page');
const cart_bag = document.getElementById('cart-bag');
const cart_close = document.getElementById('close-cart');

function menuToggel(){

    if(hamburger_icon.className == 'nav-bar-mobile-icon'){
        hamburger_icon.className = 'none';
        cancel_icon.className = 'nav-bar-mobile-icon';
        menu_item.className = 'mobile-menu-content';
    }
    else{
        hamburger_icon.className = 'nav-bar-mobile-icon';
        cancel_icon.className = 'none';
        menu_item.className = 'none';

    }

};

ticket_btn.addEventListener('click', function(){
    ticket_btn.className = "ticket-btn-click"
});

get_ticket.addEventListener('click', function(){
    get_ticket.className = "get-ticket-click"
});

contact_phone.addEventListener('click', function(){
    
    if(contact_phone_item.className == "none"){
        contact_phone_item.className = "contact-phone-item"
    }
    else{
        contact_phone_item.className = "none"
    }
});


contact_email.addEventListener('click', function(){
    
    if(contact_email_item.className == "none"){
        contact_email_item.className = "contact-email-item"
    }
    else{
        contact_email_item.className = "none"
    }
});

function cart(){
    if (cart_page.className != "cart-page"){
        cart_page.className = "cart-page"
    }
    else{
        cart_page.className = "none"
    }
}
cart_close.addEventListener('click', cart)
cart_bag.addEventListener('click',cart);



let num_ticket = document.getElementsByClassName('ticket-number')
let minus = document.getElementsByClassName('ticket-minus')
let plus = document.getElementsByClassName('ticket-plus')

let cart_minus = document.getElementsByClassName('cart-ticket-minus')
let cart_num_ticket = document.getElementsByClassName('cart-ticket-number')
let cart_plus = document.getElementsByClassName('cart-ticket-plus')


function cartItem(){
    
    $.ajax({
        url:'/events/ajax',
        type: 'get',
        success: function(res){
            $('.cart-item').text(res.number)
            
        },
    
    })
    
}

function add_fun(id){
    var csrftoken = $('input[name=csrfmiddlewaretoken]').val()
    $.ajax({
        url:'/events/cart-arthemetics/',
        type:'post',
        data: {
            action:'add',
            id:id,
            csrfmiddlewaretoken: csrftoken,
        },
        success: function(res){
            console.log("added")
        }
    })
}

function minus_fun(id){
    var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url:'/events/cart-arthemetics/',
        type:'post',
        data:{
            csrfmiddlewaretoken:csrftoken,
            id:id,
            action: 'minus'
        },
        success:function(res){
            console.log('minused')
        }
    });
}

function minusFromCookies(Id){
    my_cart[Id]['quantity'] -= 1

    if (my_cart[Id]['quantity'] <= 0){
        delete my_cart[Id]
    }
    console.log('User',user,"minus")
    document.cookie = "cart=" + JSON.stringify(my_cart) + ";domain=;path=/";

};
function addToCookies(Id){
    if (my_cart[Id] == undefined){
        my_cart[Id] = {'quantity':1}
    }
    else{
        my_cart[Id]['quantity'] +=1
    }
    
    console.log('User',user,"added")
    console.log(my_cart)

    document.cookie = "cart=" + JSON.stringify(my_cart) + ";domain=;path=/";
};

console.log(cart_num_ticket.length)
for (var x=0; x < cart_plus.length; x++){
    console.log('tyuikjn',x)
    cart_plus[x].addEventListener('click', function(){
        console.log('i was clicked')
        for (var b=0; b < cart_num_ticket.length; b++){
            console.log(this.id)
            console.log(cart_num_ticket[b])
            if(this.id == cart_num_ticket[b].id){
                console.log('next')
                let cart_num_ticket = document.getElementsByClassName('cart-ticket-number')
                let count = Number(cart_num_ticket[b].innerText)
                count += 1
                console.log('hmmmm')
                cart_num_ticket[b].innerText=count
                if(user == 'AnonymousUser'){
                    addToCookies(cart_num_ticket[b].id)
                }
                else{
                    add_fun(cart_num_ticket[b].id)
                }


            }
        }
    });
    cart_minus[x].addEventListener('click', function(){
        for (var b=0; b < cart_num_ticket.length; b++){
            if(this.id == cart_num_ticket[b].id){
                let cart_num_ticket = document.getElementsByClassName('cart-ticket-number');
                let count = Number(cart_num_ticket[b].innerText);
                if(count >= 1){
                    count += -1
                    cart_num_ticket[b].innerText=count
                    if(user == 'AnonymousUser'){
                        minusFromCookies(cart_num_ticket[b].id)
                    }
                    else{
                        minus_fun(cart_num_ticket[b].id)
                    }
                }
                else{
                    count = 0
                    cart_num_ticket[b].innerText=count
                };
                
            };
        };
    });        

};



for (var a=0; a < num_ticket.length; a++){
    
    
    plus[a].addEventListener('click', function(){
        for (var b=0; b < num_ticket.length; b++){
            if(this.id == num_ticket[b].id){
                let num_ticket = document.getElementsByClassName('ticket-number')
                let count = Number(num_ticket[b].innerText)
                count += 1
                
                num_ticket[b].innerText=count
                if(user == 'AnonymousUser'){
                    addToCookies(num_ticket[b].id)
                }
                else{
                    add_fun(num_ticket[b].id)
                }


            }
        }
    });
    minus[a].addEventListener('click', function(){
        for (var b=0; b < num_ticket.length; b++){
            if(this.id == num_ticket[b].id){
                let num_ticket = document.getElementsByClassName('ticket-number');
                let count = Number(num_ticket[b].innerText);
                if(count >= 1){
                    count += -1
                    num_ticket[b].innerText=count
                    if(user == 'AnonymousUser'){
                        minusFromCookies(num_ticket[b].id)
                    }
                    else{
                        minus_fun(num_ticket[b].id)
                    }
                }
                else{
                    count = 0
                    num_ticket[b].innerText=count
                };
                
            };
        };
    });        

};





const cart_page = document.getElementById('cart-page');
const cart_bag = document.getElementById('cart-bag');
const cart_close = document.getElementById('close-cart');

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


setInterval(cartItem, 1000);


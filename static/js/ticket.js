let num_ticket = document.getElementsByClassName('ticket-number')
let minus = document.getElementsByClassName('ticket-minus')
let plus = document.getElementsByClassName('ticket-plus')
let add = document.getElementsByClassName('add-ticket')


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


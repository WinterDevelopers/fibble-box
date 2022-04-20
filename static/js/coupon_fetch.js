const url = '/pageantry/coupon-processing'
function coupon_fetch(){
   
    let number_of_coupons = document.getElementById('coupon_num_input').value;
    let email = document.getElementById('coupon_email').value;
    let token = new Date().getTime()
    document.getElementById('token').value = token

    
    data = {'email':email, 'number_of_coupons':number_of_coupons, 'token':token}
    fetch(url, {
        method:'POST',
        headers : {
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify(data)
    })
    .then((res)=>{
        return res.json()
    })
    .then((info)=>
    console.log(info)
    )
    console.log('coupon fetch worked')
    }

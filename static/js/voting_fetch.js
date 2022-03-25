 //fetch
    
 const url = '/processing-payment'
 function my_fetch(){
     
     var counts = document.getElementById('candidate-vote-count').value
     var candidate_id = document.getElementById('candidate-id').innerHTML
     var email_value = document.getElementById('email-field').value
     let token = new Date().getTime()
     document.getElementById('token').value = token
     var data_to_be_sent = {"votes":counts, "candidate_id":candidate_id, 'email':email_value, 'token':token}

     console.log(candidate_id)
     fetch(url,{
         method:'POST',
         headers:{
             "Content-Type":"application/json",
             "X-CSRFToken":csrftoken,
         },
         body:JSON.stringify(data_to_be_sent)
     }).then((res)=>{
         return res.json()

     }).then((text)=>
         console.log(text))
     console.log('fetch worked')
 }
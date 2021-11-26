console.log('fibbleBox');

var view_button = document.querySelector(".view-button");


function view_button_func(){
    view_button.style.backgroundColor ='white';
    view_button.style.color = '#4A536B'

}

var event_office = document.querySelectorAll(".office");
var event_name = document.querySelectorAll(".name");
var i ;
var a;

//console.log(event_office)
/*for (a=0; a< event_name.length; a++){
    
    for(i = 0; i < event_office.length; i++){

        event_office[i].innerHTML

        if (event_office[i].innerHTML == event_name[a].innerHTML ){
        event_office[i].innerHTML='d'
    }
    }

    
}*/

var count_down = new Date("Dec 6, 2021 14:34:52").getTime();
console.log(count_down)

var a = setInterval(function(){
    var now = new Date().getTime();

    var difference = count_down - now;

    var days = Math.floor(difference/(1000*60*60*24));
    var hours = Math.floor((difference % (1000*60*60*24))/(1000*60*60));
    var minutes = Math.floor((difference % (1000*60*60))/(1000*60));
    var seconds = Math.floor((difference % (1000*60))/1000);

    document.getElementById('count-down').innerHTML = days + "Days: " + hours +'H: ' + minutes + 'M: ' + seconds + "S";

    if (difference < 0 ){

        clearInterval(a);

        document.getElementById('count-down').innerHTML = "ENDED"
    }
}, 1000);

var candidate_count = 0

var vote_count = document.getElementById('candidate-vote-count');
var vote_remove = document.getElementById('candidate-btn-minus');
var vote_add = document.getElementById('candidate-btn-plus');



/*vote_remove.onclick=function(){
    if (candidate_count > 1) {
        candidate_count -= 1
        vote_count.innerHTML = candidate_count
    }
    else{
        candidate_count = 0
        vote_count.innerHTML = candidate_count
    }

   
}; 


vote_add.onclick = function(){
   candidate_count += 1
    vote_count.innerHTML = candidate_count
};

console.log(candidate_count)*/

//using code to vote

var vote = document.querySelector(".candidate-code")
var code_option = document.querySelector('.code-option')
var code_option_content = document.querySelector('#code-option-content')
var code_option_close = document.querySelector('.code-option-close')

vote.onclick = function(){
    code_option.className='code-option-2';
    code_option_content.className = 'code-option-content'
    
}
code_option_close.onclick = function(){
    code_option_content.className = 'no-display'
    code_option.className=''
}

var candidate_share = document.getElementById('candidate-share')
var candidate_share_icon = document.querySelector('#candidate-share-container')

candidate_share.onclick = function(){
    candidate_share_icon.className='candidate-share-container';
}
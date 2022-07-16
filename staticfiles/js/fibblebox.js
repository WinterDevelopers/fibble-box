var done_btn = document.querySelector("#done-button")
var submit_button = document.querySelector('#submit-button')
var view_button = document.querySelector(".view-button");
console.log(done_btn)

done_btn.addEventListener('click',function(){
    this.className = "none"
    submit_button.className = "submit-email"
})


function view_button_func(){
    view_button.style.backgroundColor ='white';
    view_button.style.color = '#4A536B'

}

var pageantry_office = document.querySelectorAll(".office");
var pageantry_name = document.querySelectorAll(".name");
var i, a;


// search functionality
function simple_search(){
    let search = document.getElementById('search').value;
        search = search.toLowerCase();
    let search_list = document.getElementsByClassName("search_list")

    for(i=0; i<search_list.length; i++){
        if(!search_list[i].innerHTML.toLowerCase().includes(search)){
            search_list[i].style.display="none";

        }
        else{
            search_list[i].style.display="block"
        }
        if(search.length<1){
            search_list[i].style.display="none";
        }  
    }
}
//ends


//updating the total amount for the votes




//countdown timming







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


const search_btn = document.querySelector('#search-btn')
const search_input = document.querySelector("#search-input")
const mobile_search = document.querySelector('#mobile-search')
const search_background = document.querySelector('#search-background')
const close_search = document.querySelector('#close-search')
const search_result = document.querySelector('#search-result')
search_btn.addEventListener('click',function(e){
    mobile_search.className = 'mobile-search'
    search_background.className = 'search-background'
    search_result.className = 'search-result'
})

close_search.addEventListener('click',function(){
    mobile_search.className = 'none'
    search_background.className = 'none'
    search_result.className = 'none'
})

var searchItems =[] 
var item = document.querySelectorAll(".searchable")
item.forEach(name => {
   let item = name.outerText.toLowerCase();
   searchItems.push(item);
})

var searchResult = document.getElementById("search-result")
var searchVisible = document.getElementById("search-item")

searchItems.forEach(item =>{

    searchVisible.innerHTML+='<div class="none ddd" id="ddd">'+item+'</div>';
   
})

var test =  document.querySelectorAll('.ddd')
search_input.addEventListener('input', e =>{
    const value = e.target.value
    var i = 0
    searchItems.forEach(search_items =>{

     condition = search_items.includes(value)
     console.log(condition)
     test[i].classList.toggle('none',!condition)
        i+=1
    })
})
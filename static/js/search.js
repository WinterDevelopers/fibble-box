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
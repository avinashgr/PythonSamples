var contentDivs = ['home','menu','users','store']
// called when the body is loaded the first time page is loaded
function initialize(){
    console.log('calling the initialize')
    hide('menu');
    hide('users');
    hide('store');
}
//hides the element
function hide(el){
    var x = document.getElementById(el);
    x.style.display = 'none'
}
//shows the element
function show(el){
    var x = document.getElementById(el);
    x.style.display = 'block'
}
//show contents for current navbar item selected
function showContents(el){
    contentDivs.forEach( (div) =>{
        console.log('the value of the selected element is '+el)
        if( div === el){
            console.log('showing '+div)
            show(div)
        }else{
            console.log('showing '+div)
            hide(div)
        }
    })
}
//fetch content from the backend
const getMenuItems = async () => {
    const response = await fetch('http://localhost:5000/menu');
    const menuitems = await response.json(); //extract JSON from the http response
    console.log('the json from the backend is %j', menuitems)
}
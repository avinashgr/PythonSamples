//global variable to keep track of all items displayed
var menuitemsOnPage = []

//fetch content from the backend
const getMenuItems = async () => {
    clearMenuItemsIfFound()
    const response = await fetch('http://localhost:5000/menu');
    const menuitems = await response.json(); //extract JSON from the http response
    console.log('the json from the backend is %j', menuitems)
    displayMenuItemsToPage(menuitems)
}
//delete a menu item from the existing list 
const deleteMenuItem = async(itemid) => {
    let urlForDelete = 'http://localhost:5000/menu/'.concat(itemid)
    const response = await fetch(urlForDelete,{
        method: 'DELETE'
    })
    console.log("the response is %j",response)
    if(response){
        deleteMenuItemsFromPage(itemid)
    }
    return response.code;
}

//adds menu items passed in the function 
const displayMenuItemsToPage = (menuitems)=>{
    let menuDiv = document.querySelector('#menu-items')
    menuitems.forEach(item => {
        createMenuDiv(item, menuDiv);
    });
}

//delete menu item 
const deleteMenuItemsFromPage = (itemid)=>{
    menuitemsOnPage.forEach(item => {
        if(itemid === item){
            itemDiv = document.getElementById(itemid)
            itemDiv.remove()
        }
    });
    var filtered = menuitemsOnPage.filter(menuitem => menuitem != itemid);
    menuitemsOnPage = filtered
    console.log('the array now is %s', menuitemsOnPage)
}

//add item 
const addMenuItem = async()=>{
    let nameOfItem = document.getElementById('nameOfItem').value
    let priceOfItem = document.getElementById('priceOfItem').value
    let catOfItem = document.getElementById('catOfItem').value
    let picOfItem = document.getElementById('picOfItem').value
    urlForAddItem = 'http://localhost:5000/menu'
    menuItemToPost = {
        name: nameOfItem,
        price: priceOfItem,
        category: catOfItem,
        picture: picOfItem
    }
    const response = await fetch(urlForAddItem, {
        method: 'POST',
        mode: 'cors',
        headers: { "Content-Type": "application/json"},
        body: JSON.stringify(menuItemToPost)
    })

    return response.json();

}

const addAndRefresh = function(){
    addMenuItem().then(data=>{ 
        console.log('the response is %j', data)
        getMenuItems()
    })
}

function clearMenuItemsIfFound() {
    menuitemsOnPage = [];
    document.querySelector('#menu-items').innerHTML = '';
}

function createMenuDiv(item, menuDiv) {
    itemDiv = document.createElement('div');
    itemDiv.classList.add('menu-item');
    itemDiv.setAttribute("id", item.id);
    itemDiv.innerHTML += createMenuItemInfoDiv(item);
    button = createButtonForMenuItem(item.id);
    itemDiv.appendChild(button);
    menuDiv.appendChild(itemDiv);
    menuitemsOnPage.push(item.id);
}

function createMenuItemInfoDiv(item){
    html = '<div style="text-align:center;font-family:Arial Narrow; font-weight: bold;font-size:20px">'+item.name+'</div>'
    html = html.concat('<br><div style="text-align:center"><img src="'+item.picture+'" style="width:100p%; height:100px;object-fit:cover"></div>')
    html = html.concat('<br><div style="text-align:center;font-family:Arial Narrow;"> price($): '+item.price+'</div>')
    return html
}

function createButtonForMenuItem(itemid){
    button = document.createElement('button');
    button.innerHTML += '-';
    button.onclick = function(){
        deleteMenuItem(""+itemid);
    }
    return button
}
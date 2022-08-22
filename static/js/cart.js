var buttonInput = document.getElementsByClassName('update-cart')

for(var i = 0; i < buttonInput.length; i++){
    buttonInput[i].addEventListener('click', function(){
        //'this' represents the item that the user is clicking on 
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action', action)
        console.log('User:', user)

        if(user == 'AnonymousUser'){
            console.log('Not logged in')
        }else{
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log('User is logged in, sending data')

    //where the data the user is inputing is being sent 
    var url = '/update_item/'

    //'fetch' api to send all POST data to the backend of the application
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body : JSON.stringify({'productId' : productId, 'action' : action})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data:', data)
        //Reloads pages after data inputs by user -- FIX THIS FEATURE ASAP
        location.reload()
    })

}
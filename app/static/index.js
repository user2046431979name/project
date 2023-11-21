function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}


function pressLike(url) {
    const csrftoken = getCookie('csrftoken');
    
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        }
    })
    .then((response) => {
        let linkElement = document.getElementById('likesCount');
        let likesCount = parseInt(linkElement.innerText);
        if (response.status === 200) {
            linkElement.innerHTML = `${likesCount + 1}`;
        } else {
            linkElement.innerHTML = `${likesCount - 1}`;
        }
    });
}


async function setRating(url, rating, productId){
    const csrftoken = getCookie('csrftoken');
    await fetch( `${url}?id=${productId}&points=${rating}` , {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken, // Получаем CSRF-токен
        }});

    await fetch(`${url}${productId}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken, // Получаем CSRF-токен
        }}) 
        .then(response => response.json())
        .then(data => {
            let rating = document.getElementById('rating');
            rating.innerHTML = `${data['points']}`;
        })
}




function quantityСhange(operator){
    let quantityHtml = document.getElementById('quantity');
    let quantityInt = parseInt(quantityHtml.innerText); 
    if(operator == 'add'){
        quantityInt += 1
    }
    else if(operator != 'add' && quantityInt <= 1){
        quantityInt -= 1
    }
    quantityHtml.innerHTML = `${quantityInt}`;
}

function setShoppingCart(url, isProductDetails = false){
    const csrftoken = getCookie('csrftoken');
    let quantityInt = 1;
    if(isProductDetails){
        let quantityHtml = document.getElementById('quantity');
        quantityInt = parseInt(quantityHtml.value);   
    }

    fetch(`${url}?quantity=${quantityInt}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken, // Получаем CSRF-токен
        }}) 
}




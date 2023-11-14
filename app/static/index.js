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

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

async function setRating(url, rating, productId){
    const csrftoken = getCookie('csrftoken');
    await fetch( `${url}?id=${productId}&points=${rating}` , {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken // Получаем CSRF-токен
        }});

    await fetch(`${url}${productId}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken // Получаем CSRF-токен
        }}) 
        .then(response => response.json())
        .then(data => {
            //data['points']
            // Дайте новое значение элементу где хранится рейтинг в html
        })
}




function deleteShoppingCart(url, productId){
    fetch(`${url}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value, // Получаем CSRF-токен
        }})
        .then(()=>{
            var elementToRemove = document.getElementById(productId);
            if (elementToRemove) {
                elementToRemove.parentNode.removeChild(elementToRemove);
              } else {
                console.log('Элемент не найден');
              }
        });
}


function quantityChangeClick(operator, rowId, setProductUrl){
    // получить измененное количество(фронтенд)
    let quantityHtml = document.getElementById('quantity');
    let quantityInt = parseInt(quantityHtml.value); 

    // изменить сумму строки с учетом нового количества(фронтенд)
    let priceHtml = document.getElementById(`price_${rowId}`);
    let rowtotalpriceHtml = document.getElementById(`row_total_price_${rowId}`);
    
    rowtotalpriceHtml.textContent = `${parseFloat(priceHtml.innerText) * quantityInt}`;

    let changeRequestUrl = setProductUrl
    if (operator == 'minus'){
        changeRequestUrl = `${setProductUrl}?isMinus=true`
    }
    // отправить в базу, сохранить(запрос джанго)
    fetch(changeRequestUrl, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value, // Получаем CSRF-токен
        }})
        .then(response => response.json())
        .then(data => {
            let totalsum = document.getElementById('totalsum');
            totalsum.innerHTML = `${data['totalPrice']}`
        })

    // изменить общую на странице(фронтенд)
    
}
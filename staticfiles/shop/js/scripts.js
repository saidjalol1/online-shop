function toggleAnswer(id) {
    const answer = document.getElementById(id);
    const counter = document.getElementById(`counter-${id}`);
    answer.classList.add('deactive');
    counter.classList.add('counterAct');
    setTimeout(() => {
        answer.classList.remove('deactive');
        counter.classList.remove('counterAct');
    }, 10000);
}


function increment(element){
    // const productId = element.parentElement.dataset.productId;
    const countElement = element.previousElementSibling;
    countElement.innerText = parseInt(countElement.innerText, 10) + 1;
    
    // let url = `/add_to_cart/${productId}`
    // console.log(url);
    // const csrfToken = $('input[name=csrfmiddlewaretoken]').val();
    // $.ajax({
    //     type: "POST",
    //     url: url,
    //     headers: {
    //         'X-CSRFToken': csrfToken
    //     },
    //     success: function(response) {
    //         const countElement = element.previousElementSibling;
    //         countElement.innerText = parseInt(countElement.innerText, 10) + 1;
    //         $.ajax({
    //             type: "GET",
    //             url: "/all_data/",
    //             dataType: "json",
    //             success: function (data){
    //                 for (var item = 0; item < data.single.length; item++){
    //                     let product = document.getElementById(`id-${ data.single[item].product_id }`)
    //                     if (product){
    //                         update_order_block(data.single[item],data.total_price[0].total)
    //                         // console.log(product);
    //                     }else{
    //                         generateOrderProductBlock(data)
    //                     }
    //                 }
    //             }
    //         })
    //     },
    //     error: function(error) {
    //         console.error("Error adding to cart:", error);
    //     }
    // });
}

function decrement(element) {
    const productId = element.parentElement.dataset.productId;
    const countElement = element.nextElementSibling;
    countElement.innerText = parseInt(countElement.innerText, 10) - 1;
    // let url = `/remove_from_cart/${productId}`
    // const csrfToken = $('input[name=csrfmiddlewaretoken]').val();

    // $.ajax({
    //     type: "POST",
    //     url: url,
    //     headers: {
    //         'X-CSRFToken': csrfToken
    //     }, 
    //     success: function(context) {
    //         const countElement = element.nextElementSibling;
    //         if (parseInt(countElement.innerText) >= 0){
    //             let product = document.getElementById(`id-${productId}`)
    //             countElement.innerText = parseInt(countElement.innerText, 10) - 1;
    //             if (parseInt(countElement.innerText) == 0){
    //                 product.remove()
    //             }
    //             else{
    //                 let product_quantity = document.querySelector(`#order_quantity_${ productId }`)
    //                 let product_overall = document.querySelector(`#order_overall_${ productId }`)
    //                 let total = document.getElementById("total")
    //                 product_quantity.innerText = context.single[0].quantity
    //                 product_overall.innerText = context.single[0].overall  
    //                 total.innerText = context.total_price[0].total
    //             }
    //         }
    //     },
    //     error: function(error) {
    //         console.error("Error adding to cart:", error);
    //     }
    // });
}
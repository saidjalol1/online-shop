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
    const productId = element.parentElement.dataset.productId;
    const countCart = document.getElementById("count_cart");
    const overallSum = document.getElementById(`overall_price_${productId}`);
    const countQuantity = document.getElementById(`overall_quantity_${productId}`);
    let url = `/add_to_cart/${productId}`
    console.log(url);
    const csrfToken = $('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        type: "POST",
        url: url,
        headers: {
            'X-CSRFToken': csrfToken
        },
        success: function(response) {
            const countElement = element.previousElementSibling;
            countElement.innerText = parseInt(countElement.innerText, 10) + 1;
            console.log("Product added to cart successfully");
            console.log(countCart);
            if (response.new_added == true){
                countCart.innerText = parseInt(countCart.innerText, 10) + 1;
            } else {
                console.log("Updated Successfully");
                if (overallSum && countQuantity){
                    overallSum.innerText = parseInt(overallSum.innerText) + response.overall_sum;
                    countQuantity.innerText = parseInt(countQuantity.innerText, 10) + 1;
                } else {
                    console.log("Ishlamadi");
                }
            }
        },
        error: function(error) {
            console.error("Error adding to cart:", error);
        }
    });
}

function decrement(element){
    const productId = element.parentElement.dataset.productId;
    const countCart = document.getElementById("count_cart");
    const overallSum = document.getElementById("overall_sum");
    const countQuantity = document.getElementById("overall_quantity");
    let url = `/remove_from_cart/${productId}`
    console.log(url);
    const csrfToken = $('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        type: "POST",
        url: url,
        headers: {
            'X-CSRFToken': csrfToken
        },
        success: function(response) {
            const countElement = element.nextElementSibling;
            countElement.innerText = parseInt(countElement.innerText, 10) - 1;
            if (response.removed == true){
                countCart.innerText = parseInt(countCart.innerText, 10) - 1;
                if (response.deleted == true) {
                    location.reload()
                } else if(overallSum && countQuantity){
                    overallSum.innerText = parseInt(overallSum.innerText) - response.overall_sum;
                    countQuantity.innerText = parseInt(countQuantity.innerText) - 1;
                }
            } else {
                console.log("No Product Left in the Cart");
            }
        },
        error: function(error) {
            console.error("Error adding to cart:", error);
        }
    });
}



function addWishlist(element) {
    const productId = element.parentElement.dataset.productId;
    const countWishlist = document.getElementById("count_wishlist");
    let url = `/add_to_wishlist/${productId}`;
    const csrfToken = $('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        type: "POST",
        url: url,
        headers: {
            'X-CSRFToken': csrfToken  // Include CSRF token in request headers
        },
        success: function(response) {
            console.log("Product added to Wishlist successfully");
            console.log(countWishlist);
            // Update the wishlist count based on the response
                if (response.removed) {
                    countWishlist.innerText = parseInt(countWishlist.innerText, 10) - 1;
                    element.style.color = "black";
                } else {
                    countWishlist.innerText = parseInt(countWishlist.innerText, 10) + 1;
                    element.style.color = "red";
                }
        },
        error: function(error) {
            console.error("Error adding to wishlist:", error);
        }
    });
}

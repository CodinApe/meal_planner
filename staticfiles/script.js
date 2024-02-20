document.getElementById("addItem").addEventListener("click", function (){
    fetch('{% url 'add_food_form' %}')
    .then(function(response) {
        return response.text();
    })
    .then(function(data) {
        // Inject the add food form HTML into the page
        let addFoodFormContainer = document.getElementById("foodItemContainer");
        addFoodFormContainer.innerHTML = data;
    });
})


//get csrf token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


//Register Data


$('#registeraccount').on('click', () => {
    $('#load').addClass("fa-spinner fa-spin");
    const firstName = $('#fname').val()
    const lastName = $('#lname').val()
    const email = $('#email').val()
    const password = $('#password').val()
    const typeOfUser = $('#typeofuser').val()

    if (email.length == 0 && password.length == 0) {
        new Noty({
            type: 'warning',
            layout: 'topRight',
            text: "Enter Valid Data"
        }).show();
    } else {
        const registerData = new FormData();

        registerData.append("fname", firstName);
        registerData.append("lname", lastName);
        registerData.append("email", email);
        registerData.append("password", password);
        registerData.append("typeofuse", typeOfUser)

        axios.post('register', registerData, {
            headers: {

                "X-CSRFToken": csrftoken
            }
        }).then(res => {
            console.log(res.data);
            if (res.data.type == 'success') {
                new Noty({
                    type: 'success',
                    layout: 'topRight',
                    text: res.data.message
                }).show();
                setInterval(() => {
                    if (res.data.customer_type == "vendor") {
                        document.location.href = "vendor";
                    } else {
                        document.location.href = "/";
                    }
                }, 1200);
                $('#load').removeClass("fa-spinner fa-spin");

            } else {
                new Noty({
                    type: 'warning',
                    layout: 'topRight',
                    text: res.data.message
                }).show();
                $('#load').removeClass("fa-spinner fa-spin");

            }

        })
    }



})

//login


$('#loginbtn').on('click', () => {
    $('#load').addClass("fa-spinner fa-spin");
    
    const email = $('#loginemail').val()
    const password = $('#loginpassword').val()
    

    if (email.length == 0 && password.length == 0) {
        new Noty({
            type: 'warning',
            layout: 'topRight',
            text: "Enter Valid Data"
        }).show();
    } else {
        const registerData = new FormData();

        
        registerData.append("email", email);
        registerData.append("password", password);
        

        axios.post('login', registerData, {
            headers: {

                "X-CSRFToken": csrftoken
            }
        }).then(res => {
            console.log(res.data);
            if (res.data.type == 'success') {
                new Noty({
                    type: 'success',
                    layout: 'topRight',
                    text: res.data.message
                }).show();
                setInterval(() => {
                    if (res.data.customer_type == "vendor") {
                        document.location.href = "vendor";
                    } else {
                        document.location.href = "/";
                    }
                }, 1200);
                $('#load').removeClass("fa-spinner fa-spin");

            } else {
                new Noty({
                    type: 'warning',
                    layout: 'topRight',
                    text: res.data.message
                }).show();
                $('#load').removeClass("fa-spinner fa-spin");

            }

        })
    }



})





var selectedValue;
$('#product-attribute').change(function () {
    selectedValue = $(this).find(':selected').val();

    if (parseInt(selectedValue) == 1) {
        var html = ' <div class="form-row"><div class="col-md-6"><label for="email">Type</label><input type="text" data-type="color" class="form-control att" id="color-name" placeholder="Color" required=""></div><div class="col-md-6"><label for="review">Price</label><input type="text" data-typeprice="color" class="form-control" id="attribute-price" placeholder="Price"required=""></div></div>'

        $('.theme-form').append(html)
    } else {
        var html = ' <div class="form-row"><div class="col-md-6"><label for="email">Type</label><input type="text" data-type="size" class="form-control att" id="size-name" placeholder="Size" required=""></div><div class="col-md-6"><label for="review">Price</label><input type="text" data-typeprice="size" class="form-control" id="attribute-price" placeholder="Price"required=""></div></div>'

        $('.theme-form').append(html)
    }
})


$('#add-atributesbtn').click(() => {
    if (selectedValue == undefined) {
        var html = ' <div class="form-row"><div class="col-md-6"><label for="email">Type</label><input type="text" data-type="color" class="form-control att" id="color-name" placeholder="Color" required=""></div><div class="col-md-6"><label for="review">Price</label><input type="text" data-typeprice="color" class="form-control" id="attribute-price" placeholder="Price"required=""></div></div>'

        $('.theme-form').append(html)
    } else if (parseInt(selectedValue) == 1) {
        var html = ' <div class="form-row"><div class="col-md-6"><label for="email">Type</label><input type="text" data-type="color" class="form-control att" id="color-name" placeholder="Color" required=""></div><div class="col-md-6"><label for="review">Price</label><input type="text" data-typeprice="color" class="form-control" id="attribute-price" placeholder="Price"required=""></div></div>'

        $('.theme-form').append(html)
    } else {
        var html = ' <div class="form-row"><div class="col-md-6"><label for="email">Type</label><input type="text" data-type="size" class="form-control att" id="size-name" placeholder="Size" required=""></div><div class="col-md-6"><label for="review">Price</label><input type="text" data-typeprice="size" class="form-control" id="attribute-price" placeholder="Price"required=""></div></div>'

        $('.theme-form').append(html)
    }
})

$('#add-product-btn').click(() => {
    $('#load').addClass("fa-spinner fa-spin");
    const atrributesValue = document.querySelectorAll('.att')
    colorArray = []
    colorpriceArray = []
    sizeArray = []
    sizepriceArray = []
    price = document.querySelectorAll('#attribute-price')
    atrributesValue.forEach((attr, key) => {
        // console.log(attr.dataset.type,attr.dataset.typeprice);
        console.log(attr.value);
        console.log(price[key]);
        if (attr.dataset.type == "color" && price[key].dataset.typeprice == "color") {
            colorArray.push(attr.value)
            colorpriceArray.push(price[key].value)
        } else {
            sizeArray.push(attr.value)
            sizepriceArray.push(price[key].value)
        }



    })

    const imageFile = document.querySelector('#imagefile');
    const category = $('#main-category').val()
    const subCategory = $('#sub-category').val()
    const tag = $('#tag').val()
    const description = $('#desc').val()
    const productName = $('#product-name').val()
    const priceOfproduct = $('#price').val()
    const discount = $('#product-discount').val()
    const tax = $('#product-tax').val()

    const addProductForm = new FormData();
    addProductForm.append('image', imageFile.files[0])
    addProductForm.append('category', category)
    addProductForm.append('subcategory', subCategory)
    addProductForm.append('tag', tag)
    addProductForm.append('description', description)
    addProductForm.append('productname', productName)
    addProductForm.append('price', priceOfproduct)
    addProductForm.append('discount', discount)
    addProductForm.append('tax', tax)
    addProductForm.append('size', sizeArray)
    addProductForm.append('sizeprice', sizepriceArray)
    addProductForm.append('color', colorArray)
    addProductForm.append('colorprice', colorpriceArray)

    axios.post('vendor', addProductForm, {
        headers: {
            'Content-Type': 'multipart/form-data',
            "X-CSRFToken": csrftoken
        }
    }).then(res => {
        if (res.data.type == 'success') {
            new Noty({
                type: 'success',
                layout: 'topRight',
                text: res.data.message
            }).show();

            $('#load').removeClass("fa-spinner fa-spin");

            
            $('#tag').val("")
            $('#desc').val("")
            $('#product-name').val("")
            $('#product-discount').val("")
            
        } else {
            new Noty({
                type: 'warning',
                layout: 'topRight',
                text: res.data.message
            }).show();
            $('#load').removeClass("fa-spinner fa-spin");

        }

    })


})

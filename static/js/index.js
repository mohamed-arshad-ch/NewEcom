


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
        var html = ' <div class="form-row"><div class="col-md-6"><label for="email">Type</label><input type="text" data-type="1" class="form-control att" id="attr-name" placeholder="Color" required=""></div><div class="col-md-6"><label for="review">Price</label><input type="text" data-typeprice="color" class="form-control" id="attr-price" placeholder="Price"required=""></div></div>'

        $('.testd')
            .empty()
            .append(html)
    } else {
        var html = ' <div class="form-row"><div class="col-md-6"><label for="email">Type</label><input type="text" data-type="2" class="form-control att" id="attr-name" placeholder="Size" required=""></div><div class="col-md-6"><label for="review">Price</label><input type="text" data-typeprice="size" class="form-control" id="attr-price" placeholder="Price"required=""></div></div>'

        $('.testd')
            .empty()
            .append(html)
    }
})







$('.catnew').change(function () {
    var categoryvalue = $(this).find(':selected').val();

    const getCategoryForm = new FormData();
    getCategoryForm.append('category', categoryvalue)
    axios.post('vendor/getsubcategory', getCategoryForm, {
        headers: {

            "X-CSRFToken": csrftoken
        }
    }).then(res => {
        console.log(res.data['dict'].sub);
        $('#sub-category').empty()
        for (let index = 0; index < res.data['dict'].sub.length; index++) {
            var html = `<option value="${res.data['dict'].sub[index]}">${res.data['dict'].sub[index]}</option>`;
            $('#sub-category').append(html)



        }
    })
})
//add Product




$('#add-product-btn').click(() => {
    $('#load').addClass("fa-spinner fa-spin");

    const attrtype = document.getElementById('attr-name').dataset.type;
    const imageFile = document.querySelector('#imagefile');
    const category = $('#main-category').val()
    const subCategory = $('#sub-category').val()
    const tag = $('#tag').val()
    const description = $('#desc').val()
    const productName = $('#product-name').val()
    const priceOfproduct = $('#price').val()
    const discount = $('#product-discount').val()
    const tax = $('#product-tax').val()
    const attrname = $('#attr-name').val()
    const attrprice = $('#attr-price').val()
    const productstock = $('#product-stock').val()


    console.log(productstock);
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
    addProductForm.append('attr_name', attrname)
    addProductForm.append('attr_price', attrprice)
    addProductForm.append('attr_type', attrtype)
    addProductForm.append('stock', productstock)



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


//add Category in Admin

$('#add-category-btn').click(() => {
    $('#load').addClass("fa-spinner fa-spin");

    var newCategory = $('#new-category').val()
    var newSubCategory = $('#new-subcategory').val()
    var newTax = $('#new-tax').val()

    const newCategoryForm = new FormData();

    newCategoryForm.append('category', newCategory)
    newCategoryForm.append('subcategory', newSubCategory)
    newCategoryForm.append('tax', newTax)

    axios.post('mainadmin', newCategoryForm, {
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

            $('#load').removeClass("fa-spinner fa-spin");


            $('#new-category').val("")
            $('#new-subcategory').val("")
            $('#new-tax').val("")


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

const detailsbtn = document.querySelectorAll('#productdetails-btn');

detailsbtn.forEach((det) => {
    $(det).click(() => {
        var productId = det.dataset.productid;

        const ProductIdForm = new FormData();

        ProductIdForm.append('productid', productId)

        axios.post('mainadmin/getproductdetails', ProductIdForm, {
            headers: {
                "X-CSRFToken": csrftoken
            }
        }).then(res => {
            console.log(res.data);
            console.log(res.data.detail.subcategory);
            $('#subcategorydetails').text(res.data.detail.subcategory)
            $('#tagdetails').text(res.data.detail.tag)
            $('#descriptiondetails').text(res.data.detail.desc)
            $('#discountdetails').text(res.data.detail.discount)
            $('#attrnamedetails').text(res.data.detail.attr_name)
            $('#attrpricedetails').text(res.data.detail.attr_price)
            $('#userdetails').text(res.data.detail.user)
            console.log(res.data.detail.active);
            if (res.data.detail.active == true) {
                $('#activedetails').text("Active")

            } else {
                $('#activedetails').text("DeActive")
            }
        })
    })
})

//checkall Checkbox

const checkallbtn = document.getElementById('checkall')
const checkproductbtn = document.querySelectorAll('#checkproduct')
$(checkallbtn).click(function () {

    if ($(this).is(":checked")) {

        $(this).prop("checked", true);
        checkproductbtn.forEach((checkbtn) => {

            $(checkbtn).prop("checked", true);
        })
    } else {
        $(this).attr("unchecked");
        checkproductbtn.forEach((checkbtn) => {

            $(checkbtn).prop("checked", false);
        })
    }
})

//Active products

$('#activeproducts').click(() => {
    const ProductidArray = []
    checkproductbtn.forEach((checkbtn) => {

        if ($(checkbtn).is(":checked")) {
            const productId = checkbtn.value;
            console.log(productId)
            ProductidArray.push(String(productId))

        }
    })
    console.log(ProductidArray);
    const checkFormdata = new FormData();

    checkFormdata.append('newid', ProductidArray)

    axios.post('mainadmin/updateactive', checkFormdata, {
        headers: {
            'Content-Type': 'multipart/form-data',
            "X-CSRFToken": csrftoken
        }
    }).then(res => {
        console.log(res.data);
        document.location.href = "mainadmin";
    })

})

//set coupon code
function makeid(length) {
    var result = '';
    var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for (var i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}


$('#generate').click(() => {
    $('#co-secret').val(makeid(5))
})

//Create Coupon

$('#add-coupon-btn').click(() => {
    const coname = $('#co-name').val()
    const cosecret = $('#co-secret').val()
    const codiscount = $('#co-discount').val()
    const cocount = $('#co-count').val()
    const codate = $('#co-date').val()

    console.log(codate);

    const couponForm = new FormData()

    couponForm.append('name', coname);
    couponForm.append('secret', cosecret);
    couponForm.append('discount', codiscount)
    couponForm.append('count', cocount);
    couponForm.append('date', codate)


    axios.post('vendor/createcoupon', couponForm, {
        headers: {
            'Content-Type': 'multipart/form-data',
            "X-CSRFToken": csrftoken
        }
    }).then(res => {
        if (res.data.type == "success") {
            new Noty({
                type: 'success',
                layout: 'topRight',
                text: res.data.message
            }).show();
            var html = `<tr><th scope="row">${res.data.dict.name}</th><td>${res.data.dict.secret}</td><td>${res.data.dict.used}</td><td>${res.data.dict.count}</td><td>${res.data.dict.discount}</td><td>${res.data.dict.date}</td><td>$205</td></tr>`
            $('#coupon-body').append(html)







        } else {
            new Noty({
                type: 'warning',
                layout: 'topRight',
                text: res.data.message
            }).show();
        }

    })

})

//create uuid

function uuidv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}



//document ready

$(document).ready(() => {
    
    if (localStorage.getItem("___uuid___") === null) {
        localStorage.setItem('___uuid___', uuidv4())
        document.cookie = 'device=' + localStorage.getItem("___uuid___") + ";max-age=31536000;path=/"

    }
    


})

//add to cart 

const addtocartbtns = document.querySelectorAll('#add-to-cart');

addtocartbtns.forEach((cartbtn) => {
    $(cartbtn).click(() => {


        const cartdetails = new FormData();

        cartdetails.append('uuid', localStorage.getItem("___uuid___"));
        cartdetails.append('productid', cartbtn.dataset.prodid)

        axios.post('addtocart', cartdetails, {
            headers: {
                'Content-Type': 'multipart/form-data',
                "X-CSRFToken": csrftoken
            }
        }).then(res => {
            console.log(res.data);
        })

    })
})

//logout

$('#logoutbtn').click(() => {
    localStorage.removeItem("___uuid___");
    const logoutData = new FormData();
    axios.post('logout', logoutData, {
        headers: {
            'Content-Type': 'multipart/form-data',
            "X-CSRFToken": csrftoken
        }
    }).then(res => {
        console.log(res.data);
        document.location.href = "";
    })
})


//order status change

const productstatus = document.querySelectorAll('#product-status')

productstatus.forEach((sts)=>{
    $(sts).change(function(){
        const newproductId = sts.dataset.idval;
        const StatusValue = $(this).find(':selected').val();
        

        const StatusData = new FormData();
        StatusData.append('product-id',newproductId)
        StatusData.append('status',StatusValue)
        axios.post('vendor/changestatus', StatusData, {
            headers: {
                
                "X-CSRFToken": csrftoken
            }
        }).then(res => {
            console.log(res.data);
            
        })
    })
})
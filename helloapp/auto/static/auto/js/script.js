window.onload = OnLoadShowLike;

function OnLoadShowLike() {
    $.ajax({ url: "likedShow/", success: function (response) {
            $('.like').text(response["text"]);
            $('.like-count').text(response["likes"]);
    }})
}


$('.like').click(function () {
    $.ajax({
        url: 'liked/',
        success: function (response) {
            $('.like').text(response["text"]);
            $('.like-count').text(response["likes"]);
        },
        error: function (response) {
            console.log('error', response)
        }
    })
})

$('.change-languageBtn').click(function(){
    var url;
    if (localStorage.getItem('lan') === 'Ru'){
        url= 'change-languageEn/';
        $('.change-languageBtn').html('En');
    }
    else{
        url= 'change-languageRu/';
        $('.change-languageBtn').html('Ru');
    }
    localStorage.setItem('lan',$('.change-languageBtn').text());
    console.log(url)
    $.ajax({
        url: url,
        success: function (response) {
        },
        error: function (response) {
            console.log('error', response)
        }
    })
})
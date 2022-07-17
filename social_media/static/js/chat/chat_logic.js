function getCookie(name) {
    var cookieValue = null
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';')
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim()
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

const chats = document.querySelectorAll('.room')

chats.forEach(chat => {
    chat.addEventListener('click',function handleClick(event){
        buildDisplayChat(chat.getAttribute('value'))
        console.log('elo',event)
    })
})

function buildDisplayChat(slug){
    var chatDetails=document.getElementById('chat-details')
    var url=document.location.origin+'/chat/chat-history/'+slug

    fetch(url)
    .then((resp)=>resp.json())
    .then(function(data){
        var list=data
        for(var i in list){
            console.log(list[i])
        }
    })
}
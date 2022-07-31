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
    chat.addEventListener('click', function handleClick(event) {
        buildDisplayChat(chat.getAttribute('value'))
    })
})


function buildDisplayChat(slug) {
    var chatBox = document.getElementById('chat-box')
    var url = document.location.origin + '/chat/chat-history/' + slug

    fetch(url)
        .then((resp) => resp.json())
        .then(function (data) {
            var list = data

            chatBox.innerHTML = " "

            var chatBoxTop=`
                <h3>Chat Box:</h3>
            `
            chatBox.innerHTML+=chatBoxTop

            for (var i in list) {

                var roomId = list[i].room
                var author = list[i].user
                var timeStamp = list[i].creation_date
                var textContent = list[i].content

                var chatBoxItem = `
                <li>
                    <div class="left-info">
                        <h4>${author}</h4>
                        <p>${timeStamp}</p>
                    </div>
                    <p class="txt-content">${textContent}</p>
                </li>
                `

                document.getElementById('room-id').setAttribute('value',roomId)
                document.getElementById('room-slug').setAttribute('value',slug)

                chatBox.innerHTML += chatBoxItem

            }
        })


}

var form = document.getElementById('chat-details')
form.addEventListener('submit', function (k) {
    k.preventDefault()

    var url = document.location.origin + "/chat/message-create/"

    var message = document.getElementById('text-content').value
    var roomId = document.getElementById('room-id').value
    var textAuthor = document.getElementById('text-author').value

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'room': roomId,
            'user': textAuthor,
            'content': message
        })
    })
})


var createChatroom = document.getElementById('create-chat')

createChatroom.addEventListener('submit', function (k) {
    k.preventDefault()

    var url = document.location.origin + "/chat/chat-create/"

    var optionSelected = document.getElementById('user-selected')
    var userSelected = optionSelected.value
    var userChatCreator = document.getElementById('author').value

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'user_creating': userChatCreator,
            'user_added': userSelected
        })
    })

})

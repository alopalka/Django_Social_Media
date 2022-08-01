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

function buildChatRooms() {

    var chatHistory = document.getElementById('chat-history-ul')
    var url = document.location.origin + '/chat/chat-get/'
    const userUsername = JSON.parse(document.getElementById('user_username').textContent);

    fetch(url).then((resp) => resp.json())
        .then(function (data) {
            var list = data

            chatHistory.innerHTML = ""

            for (var i in list) {


                var roomSlug = list[i].slug
                var roomUser1 = list[i].user1
                var roomUser2 = list[i].user2

                if (roomUser1 == userUsername) {
                    roomUser = roomUser2
                } else {
                    roomUser = roomUser1
                }

                var chatRoomItem = `
                <li class="room" value="${roomSlug}">
                    <p>${roomUser}</p>
                </li>
                `

                chatHistory.innerHTML += chatRoomItem

            }

            chatBoxAddEvents()

        })

}

buildChatRooms()


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

    var roomSlug = document.getElementById('room-slug').value

    buildDisplayChat(roomSlug)
})



var createChatroom = document.getElementById('create-chat')

if (typeof (createChatroom) != 'undefined' && createChatroom != null) {
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
        
        buildChatRooms()
    })
}

function chatBoxAddEvents() {
    const chats = document.querySelectorAll('.room')

    chats.forEach(chat => {
        chat.addEventListener('click', function handleClick(event) {
            buildDisplayChat(chat.getAttribute('value'))
        })
    })
}


function buildDisplayChat(slug) {
    var chatBox = document.getElementById('chat-box')
    var url = document.location.origin + '/chat/chat-history/' + slug


    fetch(url)
        .then((resp) => resp.json())
        .then(function (data) {
            var list = data

            chatBox.innerHTML = " "

            var chatBoxTop = `
                <h3>Chat Box:</h3>
            `
            chatBox.innerHTML += chatBoxTop

            if(typeof (list.length) != 'undefined'){

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
                chatBox.innerHTML += chatBoxItem
                }
                document.getElementById('room-id').value=roomId

            }else{

                var chatBoxItem = `
                <li>
                    <div class="left-info">
                        <h4>Social Media</h4>
                        <p>00:00</p>
                    </div>
                    <p class="txt-content">${list.content}</p>
                </li>
                `
                chatBox.innerHTML += chatBoxItem

                document.getElementById('room-id').value=list.room
            }

            document.getElementById('room-slug').value=slug
    
        })


}
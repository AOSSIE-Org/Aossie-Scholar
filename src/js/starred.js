document.addEventListener('DOMContentLoaded', function () {
    chrome.runtime.sendMessage('fetchStarred', function (response) {
        for (var i = 0; i < response.data.length; i += 1) {
            const parentDiv = document.getElementById('parent-div')
            const div = document.createElement('div')
            div.setAttribute('id', 'name')
            const btn = document.createElement('button')
            btn.setAttribute('type', 'submit')
            btn.setAttribute('id', 'star-button')
            btn.textContent = response.data[i].scholarName
            div.appendChild(btn)
            parentDiv.appendChild(div)
            const image = document.createElement('img')
            image.setAttribute('id', 'picture')
            image.setAttribute('src', response.data[i].scholarImage)
            parentDiv.appendChild(image)
            const p = document.createElement('p')
            p.setAttribute('id', 'workplace')
            p.textContent = response.data[i].workplace
            const br = document.createElement('br')
            parentDiv.appendChild(br)
            parentDiv.appendChild(p)
            const br1 = document.createElement('br')
            parentDiv.appendChild(br1)
            const hr = document.createElement('hr')
            parentDiv.appendChild(hr)
        }
        addBtn(response)
    })
    function redirectToProfile(e, response) {
        const scholar = e.path[0].innerText
        for (var i = 0; i < response.data.length; i += 1) {
            if (response.data[i].scholarName === scholar) {
                chrome.runtime.sendMessage({
                    intent: 'createProfile',
                    data: response.data[i],
                })
            }
        }
    }
    function addBtn(response) {
        const button = document.getElementsByTagName('button')
        for (var i = 0; i < button.length; i++) {
            button[i].addEventListener('click', function (e) {
                redirectToProfile(e, response)
            })
        }
    }
})

let arr = []
let purpose = ''

chrome.contextMenus.create({
    id: 'AOSSIE Scholar Extension',
    title: 'Search in Google Scholar',
    contexts: ['selection'], // selection, link, image, page
})

chrome.contextMenus.onClicked.addListener((selectedText) => {
    var encodedText = selectedText.selectionText.split(' ').join('+')
    window.open('https://scholar.google.com/scholar?q=' + encodedText, '_blank').focus()
})

function createProfile() {
    chrome.tabs.create({
        url: './views/profile.html',
    })
}

function createSearchResults() {
    chrome.tabs.create({
        url: './views/search.html',
    })
}

function checkDB(data) {
    fetch(`http://127.0.0.1:8000/api/?search=${data.scholarName}+${data.workplace}`)
        .then((data) => {
            return data.json()
        })
        .then((res) => {
            const request = data
            var response = {}
            response.data = res
            if (response.data[0] === undefined) {
                fetch('http://127.0.0.1:8000/api/', {
                    method: 'POST',
                    body: JSON.stringify(request),
                }).catch((error) => console.log(error))
            } else {
                const { id } = response.data[0]
                fetch(`http://127.0.0.1:8000/api/${id}/`, {
                    method: 'PUT',
                    body: JSON.stringify(request),
                }).catch((error) => console.log(error))
            }
        })
}

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.intent === 'profileView') {
        arr = request
        purpose = 'calculateData'
        createProfile()
    }
    if (request.intent === 'search') {
        const searchTerm = request.searchTerm.split(' ').join('+')
        fetch(`http://127.0.0.1:8000/api?search=${searchTerm}`)
            .then((data) => {
                return data.json()
            })
            .then((res) => {
                var response = {}
                response.data = res
                if (response.data.length === 1) {
                    arr = response
                    purpose = 'displayData'
                    createProfile()
                } else {
                    arr = response
                    purpose = 'searchResults'
                    createSearchResults()
                }
            })
    }
    if (request.intent === 'createProfile') {
        arr = request.data
        purpose = 'showData'
        createProfile()
    }
    if (request === 'fetchSearchResults') {
        sendResponse({
            data: arr,
            intent: purpose,
        })
    }
    if (request === 'fromProfileJs') {
        sendResponse({
            data: arr,
            intent: purpose,
        })
    }
    if (request.intent === 'sendToServer') {
        sendResponse(request)
        checkDB(request)
    }
    if (request.intent === 'checkStarred') {
        fetch(`http://127.0.0.1:8000/api/?search=${request.name}+${request.work}`)
            .then((data) => {
                return data.json()
            })
            .then((res) => {
                var response = {}
                response.data = res
                if (response.data[0] === undefined) {
                    sendResponse({ isStarred: 'false' })
                } else {
                    var isStarred = response.data[0].isStarred
                    if (isStarred === true) {
                        sendResponse({ isStarred: 'true' })
                    } else {
                        sendResponse({ isStarred: 'false' })
                    }
                }
            })
    }
    if (request.intent === 'saveStarred') {
        fetch(`http://127.0.0.1:8000/api/?search=${request.name}+${request.work}`)
            .then((data) => {
                return data.json()
            })
            .then((res) => {
                var response = {}
                response.data = res
                return response.data[0].id
            })
            .then((id) => {
                contents = {
                    isStarred: true,
                }
                fetch(`http://127.0.0.1:8000/api/${id}/`, {
                    method: 'PUT',
                    body: JSON.stringify(contents),
                })
            })
    }
    if (request.intent === 'deleteStarred') {
        fetch(`http://127.0.0.1:8000/api/?search=${request.name}+${request.work}`)
            .then((data) => {
                return data.json()
            })
            .then((res) => {
                var response = {}
                response.data = res
                return response.data[0].id
            })
            .then((id) => {
                contents = {
                    isStarred: false,
                }
                fetch(`http://127.0.0.1:8000/api/${id}/`, {
                    method: 'PUT',
                    body: JSON.stringify(contents),
                })
            })
    }
    if (request === 'fetchStarred') {
        fetch('http://127.0.0.1:8000/api/?search=true')
            .then((data) => {
                return data.json()
            })
            .then((res) => {
                var response = {}
                response.data = res
                sendResponse(response)
            })
    }
    return true
})

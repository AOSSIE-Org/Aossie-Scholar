document.addEventListener('DOMContentLoaded', function () {
    chrome.runtime.sendMessage('fetchStarred', function (response) {
        console.log(response)
    })
})

document.addEventListener('DOMContentLoaded', function profile() {
    chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {

        var data = request.scriptOptions

        for (x of data.titles) {
            var d = document.getElementById('di')
            var y = document.createElement('p')
            y.innerHTML = x
            d.appendChild(y)
        }

    })

})
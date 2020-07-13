document.addEventListener('DOMContentLoaded', function profile() {
    chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {

        // var data = request.rawData

        // for (x of data.titles) {
        //     var d = document.getElementById('di')
        //     var y = document.createElement('p')
        //     y.innerHTML = x
        //     d.appendChild(y)
        // }
        console.log(request.rawData)
        console.log(request.hIndex)

    })

})
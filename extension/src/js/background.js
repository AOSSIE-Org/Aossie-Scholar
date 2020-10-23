var arr = []
var purpose = ""

function createProfile() {
    chrome.tabs.create({
        url: './views/profile.html'
    })
}

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.intent == 'profileView') {
        arr = request
        purpose = "calculateData"
        createProfile()
    }
    if (request.intent == 'search') {
        const searchTerm = request.searchTerm.split(" ").join("+")
        axios.get(`http://127.0.0.1:8000/api?search=${searchTerm}`)
            .then((response) => {
                arr = response
                purpose = "displayData"
            })
            .then(createProfile())
            .catch((error) => console.log(error, error.response))
    }
    if (request == 'fromProfileJs') {
        sendResponse({
            data: arr,
            intent: purpose
        })
    }
    if (request.intent == 'sendToServer') {
        sendResponse(request)
        axios.post('http://127.0.0.1:8000/api/', {
                "scholarName": request.scholarName,
                "scholarImage": request.scholarImage,
                "workplace": request.workplace,
                "pubCount": request.pubCount,
                "citCount": request.citCount,
                "hIndex": request.hIndex,
                "gIndex": request.gIndex,
                "mIndex": request.mIndex,
                "oIndex": request.oIndex,
                "eIndex": request.eIndex,
                "hMedian": request.hMedian,
                "sIndex": request.sIndex,
                "TNCc": request.TNCc,
                "titles": request.titles,
                "coauthors": request.coauthors,
                "citations": request.citations,
                "nCitations": request.nCitations,
                "years": request.years
            })
            .then((response) => console.log(response))
            .catch((error) => console.log(error, error.response))
    }
})
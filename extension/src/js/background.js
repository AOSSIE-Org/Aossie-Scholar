var arr=[]
var purpose = ""

function createProfile() {
    chrome.tabs.create({
        url: './views/profile.html'
    })
}

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.intent == 'profileView') {
        arr=request
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
        if(request=='fromProfileJs'){
            sendResponse({
                data: arr,
                intent: purpose
            })
        }
        if (request.intent == 'sendToServer') {
            axios.post('http://127.0.0.1:8000/api/',{
            "author_name":request.scholarName,
            "picture_url":request.scholarImage,
            "workplace":request.workplace,
            "publications":request.pubCount,
            "total_citations":request.citCount,
            "hindex":request.hIndex,
            "gindex":request.gIndex,
            "mindex":request.mIndex,
            "oindex":request.oIndex,
            "eindex":request.eIndex,
            "hmedian":request.hMedian,
            "publication_titles":request.titles,
            "citations":request.citations,
            "year":request.years
        })
            .then((response)=>console.log(response))
            .catch((error)=>console.log(error,error.response))
        }
})
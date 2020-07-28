let arr = []
let purpose = ''

function createProfile() {
    chrome.tabs.create({
        url: './views/profile.html',
    })
}

function checkDB(data) {
    axios.get(`http://127.0.0.1:8000/api/?search=${data.scholarName}+${data.workplace}`).then((response) => {
        const request = data
        if (response.data[0] === undefined) {
            axios
                .post('http://127.0.0.1:8000/api/', {
                    scholarName: request.scholarName,
                    scholarImage: request.scholarImage,
                    workplace: request.workplace,
                    pubCount: request.pubCount,
                    citCount: request.citCount,
                    hIndex: request.hIndex,
                    gIndex: request.gIndex,
                    mIndex: request.mIndex,
                    oIndex: request.oIndex,
                    eIndex: request.eIndex,
                    hMedian: request.hMedian,
                    sIndex: request.sIndex,
                    TNCc: request.TNCc,
                    titles: request.titles,
                    coauthors: request.coauthors,
                    citations: request.citations,
                    nCitations: request.nCitations,
                    years: request.years,
                })
                .catch((error) => console.log(error))
        } else {
            const { id } = response.data[0]
            axios
                .put(`http://127.0.0.1:8000/api/${id}/`, {
                    scholarName: request.scholarName,
                    scholarImage: request.scholarImage,
                    workplace: request.workplace,
                    pubCount: request.pubCount,
                    citCount: request.citCount,
                    hIndex: request.hIndex,
                    gIndex: request.gIndex,
                    mIndex: request.mIndex,
                    oIndex: request.oIndex,
                    eIndex: request.eIndex,
                    hMedian: request.hMedian,
                    sIndex: request.sIndex,
                    TNCc: request.TNCc,
                    titles: request.titles,
                    coauthors: request.coauthors,
                    citations: request.citations,
                    nCitations: request.nCitations,
                    years: request.years,
                })
                .catch((error) => console.log(error))
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
        axios
            .get(`http://127.0.0.1:8000/api?search=${searchTerm}/`)
            .then((response) => {
                arr = response
                purpose = 'displayData'
            })
            .then(createProfile())
            .catch((error) => console.log(error))
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
})

document.addEventListener('DOMContentLoaded', function () {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        chrome.tabs.sendMessage(tabs[0].id, { intent: 'showRegPanel' }, function (response) {
            if (response) {
                // Show register panel on truthy response
                const regDiv = document.getElementById('registerDiv')
                const nameInput = document.getElementById('regNameInput')

                fetch('https://countriesnow.space/api/v0.1/countries/') // Fetch from API and iterate adding options
                    .then((res) => res.json())
                    .then((jsondata) => {
                        array = jsondata.data
                        for (let i = 0; i < array.length; i++) {
                            const regSelect = document.getElementById('regCountryInput')
                            const regOption = document.createElement('option')
                            regOption.innerHTML = array[i].country
                            regOption.value = array[i].country
                            regSelect.options.add(regOption)
                        }
                    })
                    .catch((error) => {
                        console.log(error)
                    })

                nameInput.value = response.content
                regDiv.style.display = 'block'
            } else if (typeof response === 'undefined') {
                if (chrome.runtime.lastError) {
                    // We couldn't talk to the content script, it doesn't run on non-Scholar URLs
                }
            }
        })
    })

    document.getElementById('searchForm').addEventListener('submit', (e) => {
        e.preventDefault()
        const searchTerm = document.getElementById('searchInput').value
        if (searchTerm !== '' && validateInput(searchTerm) === true) {
            chrome.runtime.sendMessage({
                intent: 'search',
                searchTerm: searchTerm,
            })
        }
    })

    function validateInput(searchTerm) {
        flag = true
        for (const letter of searchTerm) {
            if (parseInt(letter)) {
                flag = false
                break
            }
        }
        return flag
    }

    function scrape(country) {
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            chrome.tabs.sendMessage(tabs[0].id, {
                intent: 'scrape',
                country: country,
            })
        })
    }

    document.getElementById('regForm').addEventListener('submit', (e) => {
        e.preventDefault()
        document.getElementById('spinlay').style.display = 'block'
        document.getElementById('spinner').style.display = 'block'

        const country = document.getElementById('regCountryInput').value
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            chrome.tabs.sendMessage(tabs[0].id, { intent: 'loadBtn' }, function (response) {
                if (response.status) {
                    document.getElementById('spinlay').style.display = 'none'
                    document.getElementById('spinner').style.display = 'none'
                    scrape(country)
                }
            })
        })
    })

    document.getElementById('star-button').addEventListener('click', () => {
        chrome.tabs.create({
            url: './views/starred.html',
        })
    })
})

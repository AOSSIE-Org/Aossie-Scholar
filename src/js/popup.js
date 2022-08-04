document.addEventListener('DOMContentLoaded', function () {
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

    document.getElementById('star-button').addEventListener('click', () => {
        chrome.tabs.create({
            url: './views/starred.html',
        })
    })
})

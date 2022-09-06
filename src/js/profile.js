function getTotalCitations(citations) {
    let sumCitations = 0
    for (let i = 0; i < citations.length; i++) {
        if (citations[i] != '') {
            sumCitations += parseInt(citations[i])
        }
    }
    return sumCitations
}

function getHindex(citations) {
    let hIndex = 0
    for (let i = 0; i < citations.length; i++) {
        if (i + 1 >= citations[i]) {
            hIndex = i + 1
            break
        }
    }
    return hIndex
}

function getGindex(citations) {
    let totalCitations = 0
    let gIndex = 0
    for (let i = 0; i < citations.length; i++) {
        totalCitations += parseInt(citations[i])
        if (Math.pow(i + 1, 2) <= totalCitations) {
            gIndex = i + 1
        } else {
            break
        }
    }
    return gIndex
}

function getMindex(years, hIndex) {
    let mIndex = 0
    currentYear = new Date().getFullYear()
    const firstPubYear = years.filter(Number).reduce((a, b) => Math.min(a, b))
    timeGap = currentYear - (parseInt(firstPubYear) + 1)
    mIndex = Number((hIndex / timeGap).toFixed(2))
    return mIndex
}

function getOindex(citations, hIndex) {
    let oIndex = 0
    let maxCitation = 0
    maxCitation = citations.reduce((a, b) => Math.max(a, b))
    const product = hIndex * maxCitation
    oIndex = Number(Math.pow(product, 1 / 2).toFixed(2))
    return oIndex
}

function getHmedian(citations, hIndex) {
    const hCore = []
    let hMedian = 0
    citations.forEach((el) => {
        if (el > hIndex) {
            hCore.push(el)
        }
    })

    function median(values) {
        if (values.length === 0) {
            return 0
        }

        values.sort(function (a, b) {
            return a - b
        })

        const half = Math.floor(values.length / 2)

        if (values.length % 2) return values[half]

        return (values[half - 1] + values[half]) / 2.0
    }
    hMedian = median(hCore)
    return hMedian
}

function getEindex(citations, hIndex) {
    let sumCitations = 0
    for (let i = 0; i < citations.length; i++) {
        if (citations[i] != '') {
            sumCitations += parseInt(citations[i])
        }
    }
    return parseFloat(Math.pow(sumCitations - Math.pow(hIndex, 2), 1 / 2).toFixed(2))
}

function getSindex(titles, citations, years) {
    sc = []
    sIndex = 0
    for (let i = 0; i < titles.length; i++) {
        if (citations[i] != '' && years[i] != '') {
            const temp = currentYear - parseInt(years[i]) + 1
            if (temp <= 5) {
                sc.push((5 / temp) * parseInt(citations[i]))
            }
            sc.push(parseInt(citations[i]))
        }
    }
    for (let i = 0; i < sc.length; i++) {
        if (i + 1 >= sc[i]) {
            sIndex = i + 1
            break
        }
    }
    return sIndex
}

function getLindex(coauthors, citations, years) {
    console.log(coauthors)
    console.log(citations)
    console.log(years)
    sum = 0
    currentYear = new Date().getFullYear()
    for (let i = 0; i < years.length; i++) {
        if (coauthors[i] != 0 && citations[i] != '' && years[i] != '') {
            ageOfPublication = currentYear - parseInt(years[i])
            if (ageOfPublication != 0) {
                sum += parseInt(citations[i]) / (coauthors[i] * ageOfPublication)
                console.log(sum)
            }
        }
    }
    lIndex = Math.log(sum) + 1
    return Math.round(lIndex * 100) / 100
}

function getARindex(citations, years) {
    sum = 0
    currentYear = new Date().getFullYear()
    for (let i = 0; i < citations.length; i++) {
        if (citations[i] != '' && years[i] != '') {
            if (i + 1 >= citations[i]) {
                break
            }
            ageOfPublication = currentYear - parseInt(years[i])
            if (ageOfPublication != 0) {
                sum += parseInt(citations[i]) / ageOfPublication
            }
        }
    }
    ARIndex = Math.sqrt(sum)
    return Math.round(ARIndex * 100) / 100
}

function getTncc(data, newnCitations) {
    let sumNCitations = 0
    for (let i = 0; i < newnCitations.length; i++) {
        sumNCitations += newnCitations[i]
    }
    return Math.round(sumNCitations * (24.66 / data) * 100) / 100
}

function getNcitations(citations, sanitized) {
    const nCitations = []
    for (let i = 0; i < citations.length; i++) {
        if (citations != '') {
            nCitations.push(Math.round(parseInt(citations[i]) / sanitized[i]))
        }
    }
    return nCitations
}

function getCitPerDoc(country) {
    return new Promise(function (resolve) {
        const url = '../lib/scimagojr.xlsx'
        const req = new XMLHttpRequest()
        req.open('GET', url, true)
        req.responseType = 'arraybuffer'
        req.onload = () => {
            const data = new Uint8Array(req.response)
            const workbook = XLSX.read(data, {
                type: 'array',
            })
            const first_sheet_name = workbook.SheetNames[0]
            const worksheet = workbook.Sheets[first_sheet_name]
            const excelData = XLSX.utils.sheet_to_json(worksheet, {
                raw: true,
            })
            for (let i = 0; i < excelData.length; i++) {
                if (excelData[i].Country === country) {
                    resolve(excelData[i]['Citations per document'])
                }
            }
        }
        req.send()
    })
}

function getScholarImage(image) {
    if (image == '/citations/images/avatar_scholar_128.png') {
        image = 'https://scholar.google.com/citations/images/avatar_scholar_128.png'
    }
    return image
}

document.addEventListener('DOMContentLoaded', function () {
    function appendToPage(response) {
        const { titles, citations, coauthors, years, nCitations } = response
        for (let i = 0; i < response.pubCount; i++) {
            if (citations[i] === undefined) {
                citations[i] = ''
            }
            if (years[i] === undefined) {
                years[i] = ''
            }
            if (nCitations[i] === undefined) {
                nCitations[i] = ''
            }
        }
        // Bind data to profile template
        document.getElementById('scholarImage').setAttribute('src', response.scholarImage)
        if (response.website !== undefined) {
            document.getElementById('website').setAttribute('href', response.website)
        }
        document.getElementById('scholarName').innerText = response.scholarName
        document.getElementById('workplace').innerText = response.workplace
        // document.getElementById('country').innerText = response.country
        document.getElementById('pubCount').innerText = response.pubCount
        document.getElementById('citCount').innerText = response.citCount
        document.getElementById('hIndex').innerText = response.hIndex
        document.getElementById('gIndex').innerText = response.gIndex
        document.getElementById('mIndex').innerText = response.mIndex
        document.getElementById('oIndex').innerText = response.oIndex
        document.getElementById('hMedian').innerText = response.hMedian
        document.getElementById('eIndex').innerText = response.eIndex
        document.getElementById('sIndex').innerText = response.sIndex
        document.getElementById('lIndex').innerText = response.lIndex
        document.getElementById('ARIndex').innerText = response.ARIndex
        document.getElementById('TNCc').innerText = response.TNCc

        let currentPage = 1
        sendData(currentPage)

        function scrollHandler() {
            const wrap = document.getElementById('tbody')
            const height = wrap.offsetHeight
            const yoffset = window.pageYOffset
            const y = yoffset + window.innerHeight
            if (y > height) {
                currentPage += 1
                sendData(currentPage)
            }
        }
        window.onscroll = scrollHandler

        function sendData(page) {
            const pagenumber = page
            const startrow = (pagenumber - 1) * 10 + 1
            const endrow = pagenumber * 10
            for (let c = startrow; c < endrow; c++) {
                if (titles[c] !== undefined) {
                    const thead = document.getElementById('tbody')
                    const tr = document.createElement('tr')
                    let titletd = document.createElement('td')
                    titletd.innerText = titles[c]
                    tr.appendChild(titletd)
                    let cittd = document.createElement('td')
                    cittd.innerText = citations[c] ? citations[c] : ''
                    tr.appendChild(cittd)
                    let coauthtd = document.createElement('td')
                    coauthtd.innerText = coauthors[c] ? coauthors[c] : ''
                    tr.appendChild(coauthtd)
                    let ncittd = document.createElement('td')
                    ncittd.innerText = nCitations[c] ? nCitations[c] : ''
                    tr.appendChild(ncittd)
                    let yrtd = document.createElement('td')
                    yrtd.innerText = years[c] ? years[c] : ''
                    tr.appendChild(yrtd)
                    thead.appendChild(tr)
                }
            }
        }
        // Check if the Scholar is starred
        // const starBtn = document.getElementById('star-button')
        // const star = document.getElementById('star')

        // chrome.runtime.sendMessage(
        //     {
        //         intent: 'checkStarred',
        //         name: response.scholarName,
        //         work: response.workplace,
        //     },
        //     function (data) {
        //         if (data.isStarred === 'true') {
        //             star.setAttribute('class', 'fas fa-star fa-4x checked')
        //         } else {
        //             star.setAttribute('class', 'fas fa-star fa-4x unchecked')
        //         }
        //     }
        // )
        // starBtn.addEventListener('click', () => {
        //     if (star.getAttribute('class') === 'fas fa-star fa-4x unchecked') {
        //         star.setAttribute('class', 'fas fa-star fa-4x checked')
        //         chrome.runtime.sendMessage({
        //             intent: 'saveStarred',
        //             name: response.scholarName,
        //             work: response.workplace,
        //         })
        //     } else {
        //         star.setAttribute('class', 'fas fa-star fa-4x unchecked')
        //         chrome.runtime.sendMessage({
        //             intent: 'deleteStarred',
        //             name: response.scholarName,
        //             work: response.workplace,
        //         })
        //     }
        // })
        // Visualise Chart
        graphYears = []
        presentYear = new Date().getFullYear()
        for (var i = presentYear - 10; i <= presentYear; i++) {
            graphYears.push(i)
        }
        var dict = {}
        for (x of graphYears) {
            count = 0
            for (y of years) {
                if (x == y) {
                    count++
                }
            }
            dict[x] = count
        }

        newDict = {}
        for (i of graphYears) {
            sum = 0
            for (var j = 0; j < response.pubCount; j++) {
                if (i == years[j]) {
                    if (citations[j] != '') {
                        sum += parseInt(citations[j])
                    }
                }
            }
            newDict[i] = sum
        }

        graphCitations = Object.values(newDict)
        graphPublications = Object.values(dict)
        let myChart = document.getElementById('myChart').getContext('2d')
        new Chart(myChart, {
            type: 'bar',

            // Dataset
            data: {
                labels: graphYears,
                datasets: [
                    // {
                    //     label: 'Publications/ Year',
                    //     backgroundColor: 'rgb(255, 99, 132)',
                    //     borderColor: 'rgb(255, 99, 132)',
                    //     data: graphPublications,
                    // },
                    {
                        label: 'Citations/ Year',
                        backgroundColor: 'rgb(231, 203, 138)',
                        borderColor: 'rgb(231, 203, 138)',
                        data: graphCitations,
                    },
                ],
            },

            // Configuration options
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    xAxes: [
                        {
                            stacked: true,
                        },
                    ],
                    yAxes: [
                        {
                            stacked: false,
                            ticks: {
                                beginAtZero: true,
                            },
                        },
                    ],
                },
            },
        })

        // data block
        const data = {
            labels: graphYears,
            datasets: [
                {
                    label: 'Publications/ Year',
                    data: graphPublications,
                    backgroundColor: [
                        'rgba(255, 51, 153, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(154, 34, 34, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(76, 0, 153, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(255, 0, 0, 0.2)',
                        'rgba(0, 255, 0, 0.2)',
                        'rgba(241, 95, 95, 0.2)',
                        'rgba(188, 229, 92, 0.2)',
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 99, 132, 1)',
                    ],
                    borderWidth: 1,
                    holeSize: 0.6,
                    animationSpeed: 0.5,
                },
            ],
        }

        // hoverLabels plugin block
        const hoverLabels = {
            id: 'hoverLabels',
            afterDatasetsDraw(chart, args, options) {
                const {
                    ctx,
                    chartArea: { top, bottom, left, right, width, height },
                } = chart
                ctx.save()

                //console.log(chart._active)

                if (chart._active[0]) {
                    //console.log(chart.config.data.labels[chart._active[0].index])
                    //console.log(chart.config.data.datasets[chart._active[0].datasetIndex].borderColor[chart._active[0].index])
                    // console.log(chart._active[0].datasetIndex)
                    // console.log(chart._active[0].index)

                    const textLabel = chart.config.data.labels[chart._active[0].index]
                    const dataLabel =
                        chart.config.data.datasets[chart._active[0].datasetIndex].data[chart._active[0].index]
                    const color =
                        chart.config.data.datasets[chart._active[0].datasetIndex].borderColor[chart._active[0].index]

                    ctx.font = 'bolder 40px Arial'
                    ctx.fillStyle = color
                    ctx.textAlign = 'center'
                    ctx.fillText(`${textLabel}: ${dataLabel}`, width / 2, height / 2 + 25)
                }
                ctx.restore()
            },
        }

        // config block
        const config = {
            type: 'doughnut',
            data: data,
            options: {
                plugins: {
                    title: {
                        display: true,
                        text: 'Publications/ Year',
                        backgroundColor: 'rgb(255, 99, 132)',
                        borderColor: 'rgb(255, 99, 132)',
                    },
                    legend: {
                        display: false,
                    },
                },
            },
            plugins: [hoverLabels],
        }

        // init render block
        const pieChart = new Chart(document.getElementById('pieChart'), config)
        var main = document.getElementById('mainbody')
        main.style.display = 'block'
        var spinner = document.getElementById('spinner')
        spinner.style.display = ' none'
        var overlay = document.getElementById('spinlay')
        overlay.style.display = ' none'
    }

    chrome.runtime.sendMessage('fromProfileJs', function (response) {
        document.title = response.data.scholarName
        if (response.intent === 'calculateData') {
            response = response.data
            newCoAuthors = []
            demoDict = {}

            for (let i = 0; i < response.coAuthors.length; i++) {
                if (typeof response.coAuthors[i] !== 'number') {
                    newCoAuthors.push(response.coAuthors[i])
                }
            }

            const sanitized = []

            const promises = []
            for (let i = 0; i < newCoAuthors.length; i++) {
                promises.push(
                    window.axios.get(`https://scholar.google.com/${newCoAuthors[i]}`).then((response) => {
                        const htmlData = response.data
                        const newString = htmlData.slice(
                            htmlData.lastIndexOf(
                                '<div id="gsc_vcd_table"><div class="gs_scl"><div class="gsc_vcd_field">Authors</div><div class="gsc_vcd_value">'
                            ) + 111,
                            htmlData.length
                        )
                        const count = newString.slice(0, newString.indexOf('</div></div>')).split(',').length
                        const url = response.config.url.slice(26, response.config.url.length)
                        demoDict[url] = count
                    })
                )
            }

            Promise.all(promises).then(() => {
                for (let n = 0; n < response.coAuthors.length; n++) {
                    if (typeof response.coAuthors[n] === 'number') {
                        sanitized.push(response.coAuthors[n])
                    } else {
                        for (const key in demoDict) {
                            if (key === response.coAuthors[n]) {
                                sanitized.push(demoDict[key])
                            }
                        }
                    }
                }

                // Compute metrics
                const { titles, citations, years, country, website } = response
                citations.sort(function (a, b) {
                    return b - a
                })

                scholarImage = getScholarImage(response.image)
                hIndex = getHindex(citations)
                gIndex = getGindex(citations)
                mIndex = getMindex(years, hIndex)
                oIndex = getOindex(citations, hIndex)
                hMedian = getHmedian(citations, hIndex)
                eIndex = getEindex(citations, hIndex)
                sIndex = getSindex(titles, citations, years)
                lIndex = getLindex(sanitized, citations, years)
                ARIndex = getARindex(citations, years)
                nCitations = getNcitations(citations, sanitized)
                sumCitations = getTotalCitations(citations)
                newCitations = response.citations.filter(Number)
                newYears = response.years.filter(Number)
                newnCitations = nCitations.filter(Number)
                getCitPerDoc(country)
                    .then((data) => getTncc(data, newnCitations))
                    .then((TNCc) => {
                        chrome.runtime.sendMessage(
                            {
                                intent: 'sendToServer',
                                scholarImage: scholarImage,
                                scholarName: response.scholarName,
                                workplace: response.workplace,
                                website: website,
                                country: country,
                                pubCount: response.titles.length,
                                citCount: sumCitations,
                                hIndex: hIndex,
                                gIndex: gIndex,
                                mIndex: mIndex,
                                oIndex: oIndex,
                                hMedian: hMedian,
                                eIndex: eIndex,
                                sIndex: sIndex,
                                lIndex: lIndex,
                                ARIndex: ARIndex,
                                titles: response.titles,
                                citations: newCitations,
                                nCitations: newnCitations,
                                TNCc: TNCc,
                                coauthors: sanitized,
                                years: newYears,
                            },
                            function (response) {
                                appendToPage(response)
                            }
                        )
                    })
            })
        }

        if (response.intent === 'displayData') {
            appendToPage(response.data.data[0])
        }
        if (response.intent === 'showData') {
            appendToPage(response.data)
        }
    })
})
module.exports = {
    getHindex,
    getEindex,
    getTotalCitations,
    getGindex,
    getMindex,
    getOindex,
    getHmedian,
    getLindex,
    getARindex,
}

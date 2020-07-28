document.addEventListener('DOMContentLoaded', function profile() {
    function appendToPage(response) {
        var titles = response.titles
        var citations = response.citations
        var coauthors = response.coauthors
        var years = response.years
        var nCitations = response.nCitations
        for (var i = 0; i < response.pubCount; i++) {
            if (citations[i] == undefined) {
                citations[i] = ""
            }
            if (years[i] == undefined) {
                years[i] = ""
            }
            if (nCitations[i] == undefined) {
                nCitations[i] = ""
            }
        }

        //Bind data to profile template
        document.getElementById('scholarImage').setAttribute('src', response.scholarImage)
        document.getElementById('scholarName').innerText = response.scholarName
        document.getElementById('workplace').innerText = response.workplace
        document.getElementById('pubCount').innerText = response.pubCount
        document.getElementById('citCount').innerText = response.citCount
        document.getElementById('hIndex').innerText = response.hIndex
        document.getElementById('gIndex').innerText = response.gIndex
        document.getElementById('mIndex').innerText = response.mIndex
        document.getElementById('oIndex').innerText = response.oIndex
        document.getElementById('hMedian').innerText = response.hMedian
        document.getElementById('eIndex').innerText = response.eIndex
        document.getElementById('sIndex').innerText = response.sIndex
        document.getElementById('sIndex').innerText = response.sIndex
        document.getElementById('TNCc').innerText = response.TNCc

        var currentPage = 1
        sendData(currentPage)

        function scrollHandler() {
            var wrap = document.getElementById('tbody')
            var height = wrap.offsetHeight
            var yoffset = window.pageYOffset
            var y = yoffset + window.innerHeight
            if (y > height) {
                currentPage += 1
                sendData(currentPage)
            }
        }
        window.onscroll = scrollHandler

        function sendData(page) {
            var pagenumber = page
            var startrow = ((pagenumber - 1) * 10) + 1
            var endrow = pagenumber * 10
            for (var c = startrow; c < endrow; c++) {
                if (titles[c] != undefined) {
                    var thead = document.getElementById('tbody')
                    var tr = document.createElement('tr')
                    var td = document.createElement('td')
                    td.innerText = titles[c]
                    tr.appendChild(td)
                    var td = document.createElement('td')
                    td.innerText = citations[c]
                    tr.appendChild(td)
                    var td = document.createElement('td')
                    td.innerText = coauthors[c]
                    tr.appendChild(td)
                    var td = document.createElement('td')
                    td.innerText = nCitations[c]
                    tr.appendChild(td)
                    var td = document.createElement('td')
                    td.innerText = years[c]
                    tr.appendChild(td)
                    thead.appendChild(tr)
                }
            }
        }

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
                    if (citations[j] != "") {
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
                datasets: [{
                    label: 'Publications/ Year',
                    backgroundColor: 'rgb(255, 99, 132)',
                    borderColor: 'rgb(255, 99, 132)',
                    data: graphPublications
                },
                {
                    label: 'Citations/ Year',
                    backgroundColor: 'rgb(231, 203, 138)',
                    borderColor: 'rgb(231, 203, 138)',
                    data: graphCitations
                }
                ]
            },

            // Configuration options
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    xAxes: [{
                        stacked: true
                    }],
                    yAxes: [{
                        stacked: false,
                        ticks: {
                            beginAtZero: true,
                        },
                    }]
                }
            }
        })

    }
    chrome.runtime.sendMessage('fromProfileJs', function (response) {
        if (response.intent == "calculateData") {
            response = response.data
            newCoAuthors = []
            demoDict = {}

            for (var i = 0; i < response.coAuthors.length; i++) {
                if (typeof (response.coAuthors[i]) != "number") {
                    newCoAuthors.push(response.coAuthors[i])
                }
            }


            var sanitized = []



            let promises = [];
            for (var i = 0; i < newCoAuthors.length; i++) {
                promises.push(
                    window.axios.get(`https://scholar.google.com${newCoAuthors[i]}`)
                        .then(response => {
                            var htmlData = response.data
                            var newString = htmlData.slice(htmlData.lastIndexOf('<div id="gsc_vcd_table"><div class="gs_scl"><div class="gsc_vcd_field">Authors</div><div class="gsc_vcd_value">') + 111, htmlData.length)
                            var count = newString.slice(0, newString.indexOf('</div></div>')).split(",").length
                            var url = response.config.url.slice(26, response.config.url.length)
                            demoDict[url] = count
                        })
                )
            }

            Promise.all(promises).then(() => {
                for (var n = 0; n < response.coAuthors.length; n++) {
                    if (typeof (response.coAuthors[n]) == 'number') {
                        sanitized.push(response.coAuthors[n])
                    } else {
                        for (let key in demoDict) {
                            if (key == response.coAuthors[n]) {
                                sanitized.push(demoDict[key])
                            }
                        }
                    }
                }

                // Compute metrics
                var citations = response.citations
                citations.sort(function (a, b) {
                    return b - a
                })
                var years = response.years

                //h-index
                var hIndex = 0
                for (var i = 0; i < citations.length; i++) {
                    if (i + 1 >= citations[i]) {
                        hIndex = i + 1
                        break
                    }
                }

                //g-index
                var totalCitations = 0
                var gIndex = 0
                for (var i = 0; i < citations.length; i++) {
                    totalCitations += parseInt(citations[i])
                    if (Math.pow(i + 1, 2) <= totalCitations) {
                        gIndex = i + 1
                    } else {
                        break
                    }
                }

                //m-index
                var mIndex = 0
                currentYear = new Date().getFullYear()
                var firstPubYear = (years.filter(Number)).reduce((a, b) => Math.min(a, b))
                timeGap = currentYear - (parseInt(firstPubYear) + 1)
                mIndex = (hIndex / timeGap).toFixed(2)

                //o-index
                var oIndex = 0
                maxCitation = citations.reduce((a, b) => Math.max(a, b))
                var product = hIndex * maxCitation
                oIndex = Math.pow(product, (1 / 2)).toFixed(2)

                //h-median
                var hCore = []
                var hMedian = 0
                citations.forEach(el => {
                    if (el > hIndex) {
                        hCore.push(el)
                    }
                })

                function median(values) {
                    if (values.length === 0) return 0;

                    values.sort(function (a, b) {
                        return a - b;
                    });

                    var half = Math.floor(values.length / 2);

                    if (values.length % 2)
                        return values[half];

                    return (values[half - 1] + values[half]) / 2.0;
                }
                hMedian = median(hCore)

                //e-index
                var sumCitations = 0
                for (var i = 0; i < citations.length; i++) {
                    if (citations[i] != "") {
                        sumCitations += parseInt(citations[i])
                    }
                }
                var eIndex = Math.pow((sumCitations - Math.pow(hIndex, 2)), (1 / 2)).toFixed(2)

                //scholar index
                sc = []
                sIndex = 0
                for (var i = 0; i < response.titles.length; i++) {
                    if (citations[i] != "" && years[i] != "") {
                        var temp = (currentYear - parseInt(years[i]) + 1)
                        if (temp <= 5) {
                            sc.push((5 / temp) * parseInt(citations[i]))
                        }
                        sc.push(parseInt(citations[i]))
                    }
                }
                for (var i = 0; i < sc.length; i++) {
                    if (i + 1 >= sc[i]) {
                        sIndex = i + 1
                        break
                    }
                }

                //Normalized Citations
                var nCitations = []
                for (var i = 0; i < citations.length; i++) {
                    if (citations != "") {
                        nCitations.push(Math.round(parseInt(citations[i]) / sanitized[i]))
                    }
                }

                newnCitations = nCitations.filter(Number)

                //TNCc
                var country = response.country
                var TNCc = 0

                function getData(country) {
                    return new Promise(function (resolve) {
                        var url = "../lib/scimagojr.xlsx";
                        var req = new XMLHttpRequest();
                        req.open("GET", url, true);
                        req.responseType = "arraybuffer";
                        req.onload = () => {
                            var data = new Uint8Array(req.response);
                            var workbook = XLSX.read(data, {
                                type: "array"
                            })
                            var first_sheet_name = workbook.SheetNames[0];
                            var worksheet = workbook.Sheets[first_sheet_name];
                            var excelData = XLSX.utils.sheet_to_json(worksheet, {
                                raw: true
                            })
                            for (var i = 0; i < excelData.length; i++) {
                                if (excelData[i]['Country'] == country) {
                                    resolve(excelData[i]['Citations per document'])
                                }
                            }

                        }
                        req.send()
                    })

                }
                getData(country).then(function (data) {
                    var sumNCitations = 0
                    for (var i = 0; i < newnCitations.length; i++) {
                        sumNCitations += newnCitations[i]
                    }
                    TNCc = sumNCitations * (24.66 / data).toFixed(3)

                    // //Changes
                    newCitations = response.citations.filter(Number)
                    newYears = response.years.filter(Number)

                    chrome.runtime.sendMessage({
                        intent: 'sendToServer',
                        scholarImage: response.image,
                        scholarName: response.scholarName,
                        workplace: response.workplace,
                        pubCount: response.titles.length,
                        citCount: sumCitations,
                        hIndex: hIndex,
                        gIndex: gIndex,
                        mIndex: mIndex,
                        oIndex: oIndex,
                        hMedian: hMedian,
                        eIndex: eIndex,
                        sIndex: sIndex,
                        titles: response.titles,
                        citations: newCitations,
                        nCitations: newnCitations,
                        TNCc: TNCc,
                        coauthors: sanitized,
                        years: newYears,
                    }, function (response) {
                        appendToPage(response)
                    })
                })

            });

        }

        if (response.intent == "displayData") {
            appendToPage(response.data.data[0])
        }
    })


})
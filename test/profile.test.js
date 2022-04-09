const puppeteer = require('puppeteer')
const extensionPath = './src/'
let browser
const extensionID = 'ikcppfgpmdnojilgipnlboojlhhemglf'

beforeAll(async () => {
    browser = await puppeteer.launch({
        headless: false, // extension are allowed only in the head-full mode
        slowMo: 100,
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            `--disable-extensions-except=${extensionPath}`,
            `--load-extension=${extensionPath}`,
        ],
    })
    pages = await browser.pages()
    pages[0].close()
})

afterAll(() => {
    browser.close()
})

test('Should redirect to star page', async () => {
    const extensionPopupHtml = 'views/popup.html'
    const page = await browser.newPage()
    await page.goto(`chrome-extension://${extensionID}/${extensionPopupHtml}`)
    const newPagePromise = new Promise((resolve) => browser.once('targetcreated', (target) => resolve(target.page())))
    await page.click('button#star-button')
    const newPage = await newPagePromise
    const testData = await newPage.$eval('body h2', (el) => el.innerText)
    expect(testData).toBe('Starred Scholars')
    await page.close()
}, 10000)

test('Should redirect to search results page', async () => {
    const extensionPopupHtml = 'views/popup.html'
    const page = await browser.newPage()
    await page.goto(`chrome-extension://${extensionID}/${extensionPopupHtml}`)
    const newPagePromise = new Promise((resolve) => browser.once('targetcreated', (target) => resolve(target.page())))
    await page.$eval('input[name=scholarName]', (el) => (el.value = 'bruno'))
    await page.click('button#searchBtn')
    const newPage = await newPagePromise
    const testData = await newPage.$eval('#search-header', (el) => el.innerText)
    expect(testData).toBe('Search Results')
    await page.close()
}, 10000)

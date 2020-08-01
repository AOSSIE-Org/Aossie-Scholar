const puppeteer = require('puppeteer')
const extensionPath = 'src'

test('new test', async () =>{
    const browser = await puppeteer.launch({
        headless: false, // extension are allowed only in the head-full mode
        slowMo: 80,
        args: [
            `--disable-extensions-except=${extensionPath}`,
            `--load-extension=${extensionPath}`
        ]
    });
    const extensionID = 'pfgmjkmlifhekiegffjndhpioapgcopk'
    const extensionPopupHtml = 'views/popup.html'
    const page = await browser.newPage();
    await page.goto(`chrome-extension://${extensionID}/${extensionPopupHtml}`);
    const title = await page.title();
    console.log(title)
    // await browser.close();
});
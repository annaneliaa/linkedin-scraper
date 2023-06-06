import * as puppeteer from 'puppeteer';
var fs = require('fs'); 

/**
 * This file contains a testing script used for HTML DOM scraping written in TypeScript.
 * It is not used in the final project but used for research purposes.
 * The script uses the Puppeteer library to open a Chrome browser and navigate to a LinkedIn profile page.
 * Logging in is done with the use of the Linkedin Session cookie, which is copied from the browser and pasted into the script.
 * It then takes a screenshot of the page and saves it as a .png file.
 */

const LI_AT = 'AQEDAUMeSlEFOGavAAABh-NMiI8AAAGIK2bTiE0ASl8Tu-FSEVXXMhWE11lL9x49Ns2gxl0BWLESGMNLl23V5XJE38eFM4al5s4AWXJwqeq0f1_5YOCYJqJH4IMBC2_wh51hSTGGiuc42PmEupo4gV5A'

const sleep = (ms: number) => new Promise(r => setTimeout(r, ms));

/* This code block is using the Puppeteer library to launch a new instance of the Chromium browser and
create a new page object. The `headless` option is set to `false`, which means that the browser
window will be visible during the script's execution. The `executablePath` option specifies the path
to the Chromium executable. The `await` keyword is used to wait for the browser and page objects to
be created before continuing with the script's execution. */
(async () => {
    const browser = await puppeteer.launch({
        headless: false,
        executablePath: '/opt/homebrew/bin/chromium'
      })    
    const page = await browser.newPage();

    /* This code is setting a cookie named 'li_at' with a value of LI_AT (which is a LinkedIn session
    token) for the domain 'www.linkedin.com'. The cookie is set to expire in one year from the
    current date and is set for the root path '/'. This is done so that the script can access the
    LinkedIn profile page without having to log in manually. */
    await page.setCookie({
        name: 'li_at',
        value: LI_AT,
        domain: 'www.linkedin.com',
        path: '/',
        expires: Date.now() + 1000 * 60 * 60 * 24 * 365
    })

    /* This URL is used for testing */
    const url = 'https://www.linkedin.com/in/annavisman/'

    /* `await page.goto(url)` navigates the browser to the specified URL, which in this case is the
    LinkedIn profile page of a user. */
    await page.goto(url);
    await page.setViewport({
        width: 1200,
        height: 800
    });

    /* `page.evaluate(() => { window.scrollBy(0, window.innerHeight); });` is a function that is
    executed in the context of the current page. It scrolls the page down by the height of the
    current viewport. */
    page.evaluate(() => {
        window.scrollBy(0, window.innerHeight);
      });

    await sleep(10000);

    /* `await page.screenshot()` is a function provided by the Puppeteer library that takes a
    screenshot of the current page and saves it as an image file. In this case, it is taking a
    screenshot of the LinkedIn profile page and saving it as a .png file with the name
    'profile.png'. The `fullPage` option is set to `true`, which means that the entire page will be
    captured in the screenshot, including any content that is not visible in the current viewport. */
    await page.screenshot({
        path: 'profile.png',
        fullPage: true
    });

    /* `await page.pdf({path: 'linkedin.pdf'});` is a function provided by the Puppeteer library that
    generates a PDF file of the current page and saves it to the specified file path. In this case,
    it is generating a PDF file of the LinkedIn profile page and saving it as 'linkedin.pdf'. */
    await page.pdf({path: 'linkedin.pdf'});
    
    await sleep(10000);

    /* `await browser.close();` is a function call that closes the Chromium browser instance that was
    launched by the script. The `await` keyword is used to wait for the browser to close before continuing with the script's
    execution. */
    await browser.close();
})();



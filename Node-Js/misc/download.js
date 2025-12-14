//make it configurable
window.timeBetweenDownloads = (x) => Math.max(x*160, 3000)
window.minFileSizeMb = 0.1;
window.maxFileSizeMb = 3000;
window.shouldScroll = true;
window.shouldUnroll = true;

function leftClick(element) {
    const contextMenuEvent = new MouseEvent('contextmenu', {
        bubbles: true, cancelable: true, view: window,
        button: 2, // Right mouse button
        buttons: 2, // Indicates the right button is pressed
        clientX: element.getBoundingClientRect().left + element.offsetWidth / 2, // Approximate center of the element
        clientY: element.getBoundingClientRect().top + element.offsetHeight / 2
    });
    element.dispatchEvent(contextMenuEvent);
}

function allBookcards() { return Array.from(document.querySelectorAll('z-bookcard')); }

let filters2 = {
    isDeleted(b) { return b.getAttribute('deleted') == 1 },

    fileSizeToSmall(b) {
        const fs = parseFilesizeToMB(b.getAttribute('filesize'));
        return fs < window.minFileSizeMb || fs > window.maxFileSizeMb;
    },

    missingDownload(b) {
        let dl = b.getAttribute('download');
        return dl == null || dl == "undefined"
    },

    notEnglishOrEmpty(b) {
        let lang = b.getAttribute('language');
        return  lang != 'english' && lang != '';
    },

    hasBeenDownloaded(b) {
        return b.shadowRoot.querySelector("z-cover").shadowRoot.querySelector(".mark.downloaded") != undefined;
    },
};

function appFilter2(b) { return Object.keys(filters2).filter(name => filters2[name](b)); }

function outline(card, oval) { card.shadowRoot.querySelector('div').style.outline = oval; }

function parseFilesizeToMB(filesizeStr) {
    if (!filesizeStr) return 0;

    // Usuwamy wszystkie spacje i konwertujemy na lowercase
    const normalized = filesizeStr.replace(/\s+/g, ' ').toLowerCase();

    // Szukamy liczby i jednostki
    const match = normalized.match(/([0-9.,]+)\s*(kb|mb|gb)/);
    if (!match) return 0;

    const value = parseFloat(match[1].replace(',', '.'));
    const unit = match[2];

    // Konwertujemy na MB
    switch (unit) {
        case 'kb': return value / 1024;
        case 'mb': return value;
        case 'gb': return value * 1024;
        default: return 0;
    }
}

let delay = (s) => new Promise(resolve => {setTimeout(resolve, s) });
async function download(cards) {
    let prevCard = cards[0];
    let len = cards.length;

    for (const [idx, card] of cards.entries()) {
        outline(prevCard, '');
        outline(card, "thick solid #0000FF");
        card.style.outline = 'red solid 2px';
        prevCard = card;
        if (window.shouldScroll) card.scrollIntoViewIfNeeded();
        let filesizeMB = parseFilesizeToMB(card.getAttribute('filesize'));

        console.warn(`working on [${idx}/${len}]:`, card);
        //let url = card.getAttribute('download');
        await downloadFileAlter(card);
        //CurrentUser.addDownloadedBook(card.id);
        await delay(window.timeBetweenDownloads(filesizeMB));
    }
    console.warn("finished downloading.");
}

async function downloadFileAlter(b) {
    leftClick(b.shadowRoot.querySelector(".tile"));
    await delay(500);
    let btn = document.querySelector(".zlib-context-element.icon-zlibicon-bookcard-download")
    if (btn != undefined) btn.click();
    else console.warn("skip due to missing download button!", b);
}

async function unroll() {
    let m = document.querySelector(".page-load-more");
    if (m) {
        if (window.shouldScroll) m.scrollIntoViewIfNeeded();
        m.click()
        await delay(2000);
        await unroll();
    }
}

function downloadFile(url) {
    var downloadLink = document.createElement("a");
    downloadLink.href = window.location.origin + url;
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
}



function downloadAuto() {
    let toD = toDownload();
    download(toD);
}

function toDownload() {
    let cards = allBookcards();
    let cardsF = cards.map(item => {
        let err = appFilter2(item);
        let willDownload = err.length == 0;
        return { err, item, willDownload };
    });
    let toDownload = cardsF.filter(s => s.willDownload).map(s => s.item);
    console.warn({cardsF, toDownload});
    return toDownload;
}

async function main() {
    if (!window.shouldUnroll) console.warn("skip unroll (due to shouldUnroll=false)!");
    else await unroll();
    downloadAuto();
}

main();

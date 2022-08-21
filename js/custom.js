window.onload = function () {
    let mode = document.getElementsByClassName("mode")[0];
    mode.onclick = function () {
        const modeImages = ["images/sun.png", "images/moon.png"];
        const modeCssUrl = [
            "css/github-markdown-light.css",
            "css/github-markdown-dark.css",
        ];
        let currentBackgroundImage = getStyle(mode, "backgroundImage").match(
            /images[^"]*/
        )[0];
        let nextIndex = (modeImages.indexOf(currentBackgroundImage) + 1) % 2;

        // toggle background image
        mode.style.backgroundImage = 'url("' + modeImages[nextIndex] + '")';
        // toggle css
        toggleCss(modeCssUrl[nextIndex]);
    };
};

function getStyle(obj, name) {
    return window.getComputedStyle
        ? getComputedStyle(obj, null)[name]
        : obj.currentStyle[name];
}

// toggle css file
function toggleCss(newCssUrl) {
    let link = document.querySelector("link[href^='css/github-markdown']");
    link.href = newCssUrl;
}

// load external css file
function loadCss(url) {
    var head = document.getElementsByTagName("head")[0];
    var link = document.createElement("link");
    link.type = "text/css";
    link.rel = "stylesheet";
    link.href = url;
    head.appendChild(link);
}

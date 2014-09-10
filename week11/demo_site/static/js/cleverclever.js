var CLEVERCLEVER = function () {

    function Link(name, uri) {
        element = document.createElement("a");
        element.href = uri;
        t = document.createTextNode(name);
        element.appendChild(t);
        document.body.appendChild(element);
    }

    function addUrl(link) {
        Link(link[0], link[1]);
    }

    function init(links) {
        links.forEach(addUrl);
    }

    return {
        init: init
    }
}();
var CLEVERCLEVER = function () {
    var doc = document,
        target = doc.body;

    create = function (s) {
        return doc.createElement(s)
    };

    text = function (s) {
        return doc.createTextNode(s)
    };

    add = function (element) {
        return target.appendChild(element);
    };

    br = function () {
        add(create("br"));
    };

    Link = function (name, uri) {
        element = create("a");
        element.href = uri;
        t = text(name);
        element.appendChild(t);
        add(element);
    };

    function addUrl(link) {
        Link(link[0],link[1]);
        br();
    }

    function init(links) {
        links.forEach(addUrl);
    }

    return {
        init: init
    }
}();
CLEVERCLEVER.init(
    [
        ["admin", "admin"],
        ["list", "list"],
        ["add", "/admin/demo_app/event/add/"]
    ]
);
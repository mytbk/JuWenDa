var titHeight = 0;

function initDetail() {
    titHeight = $('#header').offset().height;
    appcan.frame.open("content", "details_content.html", 0, titHeight);
    window.onorientationchange = window.onresize = function() {
        appcan.frame.resize("content", 0, titHeight);
    }

    appcan.button(".nav-btn", "btn-act", function(a, b) {
        appcan.closeWin(-1);
    })
}

function common() {
    titHeight = $('#header').offset().height;
    var s = window.getComputedStyle($("#content")[0], null);
    var ft = window.getComputedStyle($("#footer")[0], null);
    var h = titHeight + parseInt(ft.height);
    uexWindow.openPopover("articlecommon", "0", "articlecommon.html", "", 0, 0, parseInt($('#content').offset().width), '', parseInt(s.fontSize), "0", 0);

    //appcan.openPopoverByEle('page_0', 'articlecommon.html', 0, 0, 'articlecommon')
    //uexWindow.openPopover("articlecommon","0","articlecommon.html","",int(x),int(y),int(s.width),int(s.height),int(s.fontSize),"0");
}

function closepop() {
    appcan.closePopover("articlecommon");
}
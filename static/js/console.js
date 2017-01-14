// Console.log
if (window.console) {
    var cons = console;
    if (cons) {
        cons.log("%c \n\
 ___ _            _   _       _ _\n\
|_ _| |_ ___ _ __| \\ | |_   _| | |\n\
 | || __/ _ \\ '__|  \\| | | | | | |\n\
 | || ||  __/ |  | |\\  | |_| | | |\n\
|___|\\__\\___|_|  |_| \\_|\\__,_|_|_|\n\
\n\
By ZMOM1031\n\
https://www.iternull.com/\n\
\n\
","color: #00adef;");
    }
}

// Change Title
/*
var changeTitle = {
	originTitle: document.title,
	change: function() {
		document.title = "(,,#ﾟДﾟ) Browser is Crash";
	},
	reset: function() {
		document.title = changeTitle.originTitle;
	}
};
document.addEventListener('visibilitychange', function() {
    if (document.hidden) {
        changeTitle.change();
    } else {
        changeTitle.reset();
    }
});
*/

// Change Title
var titleTime = document.title
function originTitle(){
	document.title = titleTime,
	$('[rel="shortcut icon"]').attr("href", "/favicon.ico");
}
function changeTitle(){
	document.title = "(,,#ﾟДﾟ) Browser is Crash",
	$('[rel="shortcut icon"]').attr("href", "/theme/img/fail.ico");
}
function resetTitle(){
	document.title = "(/≧▽≦/)咦！又好了！" + titleTime,
	$('[rel="shortcut icon"]').attr("href", "/favicon.ico");
}
document.addEventListener('visibilitychange', function() {
    if (document.hidden) {
        changeTitle();
    } else {
        resetTitle(),
		setTimeout("originTitle()", 1e3);
    }
});

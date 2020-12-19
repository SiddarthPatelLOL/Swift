chrome.runtime.onInstalled.addListener(function() {
    chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {
        chrome.declarativeContent.onPageChanged.addRules([{
        conditions: [new chrome.declarativeContent.PageStateMatcher({
            // TO DO: ShowPageAction called only when Twitch URL path specifies an actual twitch user via Twitch API
            pageUrl: {urlPrefix: 'https://www.twitch.tv/'},
        })
        ],
            actions: [new chrome.declarativeContent.ShowPageAction()]
        }]);
    });

});
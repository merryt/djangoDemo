var newQuotes = () =>{
    var request = new XMLHttpRequest();
    request.open('GET', jsonPath, true);

    request.onload = function() {
        if (request.status >= 200 && request.status < 400) {
            // Success!
            var data = JSON.parse(request.responseText);
            renderQuotes(data, 3)
        } else {
            // We reached our target server, but it returned an error

        }
    };

    request.onerror = function() {
    // There was a connection error of some sort
    };

    request.send();
}

function copy(o) {
    var output, v, key;
    output = Array.isArray(o) ? [] : {};
    for (key in o) {
        v = o[key];
        output[key] = (typeof v === "object") ? copy(v) : v;
    }
    return output;
 }


var renderQuotes = (quotes, numberToRender) => {
    quotesToRender = quotes.slice(0) // deep clones so we don't the original data
    while(quotesToRender.length > numberToRender){
        randomQuoteIndex = Math.floor(Math.random() * quotesToRender.length)
        quotesToRender.splice(randomQuoteIndex, 1)
    }
    for(var i = 0; i < quotesToRender.length; i++){
        renderQuote(quotesToRender[i])
    }
}

var renderQuote = (quote) => {
    var quoteTemplate = document.querySelector('#quoteTemplate');  
    quoteTemplate.content.querySelector('.companyName').innerText = quote.CompanyName;  
    quoteTemplate.content.querySelector('.exchangeName').innerText = quote.ExchangeName;  
    quoteTemplate.content.querySelector('.price').innerText = quote.CurrentPrice.Amount;  
    quoteTemplate.content.querySelector('.difference').innerText = quote.Change.Amount;  
    var clone = document.importNode(quoteTemplate.content, true);  
    document.getElementById("quotes-box").appendChild(clone);  
}

newQuotes();
newQuotes();
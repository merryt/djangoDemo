var newQuotes = () =>{
    var request = new XMLHttpRequest();
    request.open('GET', jsonPath, true);

    request.onload = function() {
        if (request.status >= 200 && request.status < 400) {
            // Success!
            var data = JSON.parse(request.responseText);
            numberOfQuotesToRender = 3
            renderQuotes(data, numberOfQuotesToRender)
        } else {
            // We reached our target server, but it returned an error

        }
    };

    request.onerror = function() {
    // There was a connection error of some sort
    };

    request.send();
}

var renderQuotes = (quotes, numberToRender) => {
    document.querySelector('#quotesBox').innerHTML = "";
    quotes = quotes.randomize();
    quotes = quotes.slice(0,3);
    for(var i = 0; i < quotes.length; i++){
        renderQuote(quotes[i])
    }
}

var renderQuote = (quote) => {
    var quoteTemplate = document.querySelector('#quoteTemplate');  
    quoteTemplate.content.querySelector('.companyName').innerText = quote.CompanyName;  
    quoteTemplate.content.querySelector('.symbol').innerText = quote.Symbol;  
    quoteTemplate.content.querySelector('.price').innerText = quote.CurrentPrice.Amount;  
    quoteTemplate.content.querySelector('.difference').innerText = quote.Change.Amount + "%";  
    quoteTemplate.content.querySelector('.difference').classList.toggle("negative", quote.Change.Amount < 0);
    var clone = document.importNode(quoteTemplate.content, true);  
    document.querySelector("#quotesBox").prepend(clone);  
}

newQuotes();

document.querySelector("#rerenderQuotes").onclick = function(){
    newQuotes();
}

/// randomize array helper function
Array.prototype.randomize = function() 
{
  var arr = [];
  for(var i = 0, len = this.length; i<len; ++i)
  {
    var pos = Math.floor(Math.random() * (i + 1));
    arr.splice(pos,0,this[i]);    
  }
  return arr;
};

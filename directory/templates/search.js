var documents = [{
    "name": "Lunr",
    "text": "Like Solr, but much smaller, and not as bright."
  }, {
    "name": "React",
    "text": "A JavaScript library for building user interfaces."
  }, {
    "name": "Lodash",
    "text": "A modern JavaScript utility library delivering modularity, performance & extras."
  }] //FORMAT IS IMPORTANT

var idx = lunr(function () {
  this.ref('name')
  this.field('name')
  this.field('text')

  documents.forEach(function (doc) {
      this.add(doc)
  }, this)
})

var tokenLengthMetadata = function (builder) {
    // Define a pipeline function that stores the token length as metadata
    var pipelineFunction = function (token) {
      token.metadata['tokenLength'] = token.toString().length
      return token
    }

    // Register the pipeline function so the index can be serialised
    lunr.Pipeline.registerFunction(pipelineFunction, 'tokenLenghtMetadata')

    // Add the pipeline function to the indexing pipeline
    builder.pipeline.before(lunr.stemmer, pipelineFunction)

    // Whitelist the tokenLength metadata key
    builder.metadataWhitelist.push('tokenLength')
  }

//idx.search('title:foo') //restrict
//idx.search('foo^10 bar') //boost
//idx.search('foo~1') //fuzzy
function result() {
    var returnRes = [];
    var written=false;
    var printState = "";
    var searchTerm = String(document.getElementById("txtInput").value);
    if (searchTerm==(""))
    {
        document.getElementById("resultPar").innerHTML="nothing found";
    }
    else{
        searchTerm="name:" + searchTerm + " " + searchTerm + "~2";
        console.log("This is the search term: " + searchTerm);
        var result=idx.search(searchTerm)
        //console.log(result)
        for(var i = 0; i<result.length; i++)
        {
            if(result[i]['score']>0.2) {
                //console.log(result[i]['ref']+".exe");
                printState+=(result[i]['ref']+".exe");
                printState+=("<br>");
                written=true;
                returnRes[i]={name: result[i]['ref']+".exe"};
            }
            document.getElementById("resultPar").innerHTML=printState;
        }
        if(written==false)
        {
            document.getElementById("resultPar").innerHTML="nothing found";
        }
        else
        {
            for(var i = 0; i<result.length; i++)
            {
                console.log(returnRes[i]['name']);
            }

        }
    }
}

//HOW TO USE: Replace any "resultPar" with a element you want to update with
//            search results. After that, simply link an input on keyup to
//            this function. See indexer.html for details/example.
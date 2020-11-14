var listed = [{'name': 'yo', 'link': "https://tse4.mm.bing.net/th?id=OIP.lnQOZq_04T6rE32FCVrDggHaHC&pid=Api&P=0&w=171&h=163"}, {'name': 'ppooy', 'link': "https://search.yahoo.com/search?fr=mcafee&type=E211US550G0&p=how+to+change+the+text+of+an+html+element"}, {'name': 'aay', 'link': "https://search.yahoo.com/search?fr=mcafee&type=E211US550G0&p=how+to+change+the+text+of+an+html+element"}];
//Put actual data in listed

function myFunction() {
  // Declare variables
  var input, filter, ul, li, a, i;
  input = document.getElementById("mySearch");
  filter = input.value.toUpperCase();
  ul = document.getElementById("myMenu");
  li = ul.getElementsByTagName("li");

  console.log(input.value);
  var counter=0;
  for(i = 0; i < listed.length; i++)
  {
      var currentId=("myMenu" + String(counter));
      var bruh = document.getElementById(currentId);
      var name = listed[i]['name'];
      var link = listed[i]['link'];
      console.log(name.toUpperCase().indexOf(filter) > -1);
      if (name.toUpperCase().indexOf(filter) > -1 && counter<8)
      {
        bruh.style.display = "block";
        li[counter].style.display = "block";
        bruh.href=link;
        bruh.innerHTML=name;
        console.log("loaded "+name);
        counter++;
      };
  }
  var countered=counter;

  while(counter<8)
  {
    var currentId=("myMenu" + String(counter));
    var bruh = document.getElementById(currentId);
    bruh.style.display = "none";
    li[counter].style.display = "none";
    counter++;
  }

  if(countered==0)
  {
    console.log("EXTRAFUNCTION: Counter");
    var currentId=("myMenu" + String(countered));
    var bruh = document.getElementById(currentId);
    bruh.href='#';
    bruh.style.display = "block";
    li[countered].style.display = "block";
    bruh.innerHTML="No results found.";
  }

  if(input.value=="")
  {
    console.log("EXTRAFUNCTION: Blanker");
    console.log(li.length);
    for (i = 0 ; i < li.length-1; i++)
    {
        var caller = ("myMenu" + String(i));
        console.log(caller);
        var bruh = document.getElementById(caller);
        console.log(bruh);
        bruh.style.display = "none";
        li[i].style.display = "none";
    }
  }
  console.log(counter);
  console.log('-----------------------BREAK-----------------------');
}
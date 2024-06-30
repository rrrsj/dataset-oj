function add_page_list()
{
    var list=document.getElementById('l1');
    var url = window.location.href;
    var page=getQueryString("p");
    if(page==null)
    {
        page = 0;
    }
    else
    {
        page= Number(page);
    }
    var ele='<li> <a href="http://127.0.0.1:5000/main?p='+(page-1).toString()+'" aria-label="Previous"> <span aria-hidden="true">&laquo;</span> </a> </li>';
    for(var i=0;i<=5;i++)
    {
        //console.log((page+i).toString());
        ele=ele+'<li><a href="http://127.0.0.1:5000/main?p='+(page+i).toString()+'">'+(page+i).toString()+'</a></li>';
    }
    ele=ele+'<li> <a href="http://127.0.0.1:5000/main?p='+(page+i).toString()+'" aria-label="Next"> <span aria-hidden="true">&raquo;</span> </a> </li>';
    list.innerHTML=ele;
}

function getQueryString(name) {
var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
var r = window.location.search.substr(1).match(reg);
if (r != null) return unescape(r[2]); return null;
}
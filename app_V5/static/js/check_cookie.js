function check_cookie()
{

    console.log(document.cookie)
    data={'cookie':document.cookie};
    var input = JSON.stringify(data);
    request('post',"http://127.0.0.1:5000/check_user_cookie",input,de_cookie);
}
function de_cookie(res)
{
    if(res['state']==0)
    {
        document.cookie = "user=";
        console.log(res)
        if(window.location.href!="http://127.0.0.1:5000/log_in")
        {
            console.log(res)
            location.href = "http://127.0.0.1:5000/log_in";
        }
    }
}
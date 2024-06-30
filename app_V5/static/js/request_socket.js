function request(type,url,input,success_function)
{

    $.ajax({
        type:type,
        url:url,
        async:true,
        dataType:"json",
        data: input,
        success:success_function
    })
}
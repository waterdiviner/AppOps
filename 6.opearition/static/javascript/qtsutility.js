//convert unicode to char for chinese
function unicode2Char(json_str){
    str = unescape(json_str.replace(/u/g,"%u").replace(/\\/g,""));
    str = str.replace(/%u/g,"");
    return str;
}

//convert string to json obj
function make_json_from_str(json_str){
    return eval("(" + unicode2Char(json_str) + ")");
}

//get value field by id field form json
function get_json_value(key,json_str,f_id,f_value){
    var value = '';
    var obj = make_json_from_str(json_str);
    for(i = 0;i < obj.length;i++){
        if(obj[i][f_id] == key){
            value = obj[i][f_value];
            break;
        }
    }
    return value;
}
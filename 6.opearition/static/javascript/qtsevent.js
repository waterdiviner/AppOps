function onComboboxLoadSuccess(obj){
    if(obj.combobox('getData').length){
        obj.combobox('select',obj.combobox('getData')[0]['id']);
    }
}
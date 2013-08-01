function sendCnpj(){
	input = document.forms["form"].query.value
    cnpj = input.replace(/[^0-9]/g, "")
    return true;
}
    
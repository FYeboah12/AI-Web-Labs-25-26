// Frances Yeboah P7
let alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
const isLowerCase = str => str === str.toLowerCase();
//problem 1
function caesarCipher(message, shift){
	message = Array.from(message);
	newMessage = message.map(letter => {
	if (alpha.indexOf(letter.toUpperCase()) == -1){
		return letter;
	}else{
		return alpha.charAt((alpha.indexOf(letter.toUpperCase()) + shift) % 26);
	}})
	for (let i = 0; i < newMessage.length; i++){
	    if(isLowerCase(message[i]))
	        newMessage[i] = newMessage[i].toLowerCase()
	}
return newMessage.join('');
}
//problem 2
function caesarDecode(message, shift){
	message = Array.from(message);
	newMessage = message.map(letter => {
	if (alpha.indexOf(letter.toUpperCase()) == -1){
		return letter;
	}else{
		return alpha.charAt((26 + alpha.indexOf(letter.toUpperCase()) - shift) % 26);
	}})
	for (let i = 0; i < newMessage.length; i++){
	    if(isLowerCase(message[i]))
	        newMessage[i] = newMessage[i].toLowerCase()
	}
return newMessage.join('');
}
//problem 3
function generateCipher(){
    let indices = []
    while (indices.length < 26){
      index = Math.floor(Math.random() * 26);  
      if(! indices.includes(index)){
          indices.push(index)
      }
    }
	let randomCipher = {}
	for (let i = 0; i < 26; i++){
	    randomCipher[alpha[i]] = alpha[indices[i]]
	}
	return randomCipher
}
//problem 4
function substitutionCipher(message, cipherMap){
	newMessage = Array.from(message)
	newMessage = newMessage.map(letter => {
	if (alpha.indexOf(letter.toUpperCase()) == -1){
		return letter;
	}else{
		return cipherMap[letter.toUpperCase()];
	}})
	for (let i = 0; i < newMessage.length; i++){
	    if(isLowerCase(message[i]))
	        newMessage[i] = newMessage[i].toLowerCase()
	}
    return newMessage.join('');
}

//problem 5
function substitutionDecode(message, cipherMap){
	newMessage = Array.from(message)
	newMessage = newMessage.map(letter => {
	if (alpha.indexOf(letter.toUpperCase()) == -1){
		return letter;
	}else{
		for (key in cipherMap){
			if (cipherMap[key] == letter.toUpperCase())
			return key;
		}	
	}})
	console.log(newMessage)
	for (let i = 0; i < newMessage.length; i++){
	    if(isLowerCase(message[i]))
	        newMessage[i] = newMessage[i].toLowerCase()
	}
    return newMessage.join('');
}

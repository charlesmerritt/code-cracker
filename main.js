function enterpass(password) {
	var form = document.querySelector('#paste');
	// Alerts.hideAll();

	try {
		sjcl.decrypt(password, sjcl.codec.utf8String.fromBits(sjcl.codec.base64.toBits(form.pasteText.value)), {ks: 256});
		return true;
	} catch (e) {
		// console.error(e);
		// if (e.message && e.message === 'ccm: tag doesn\'t match') {
		// 	Alerts.show('Unsuccessful, password is incorrect.');
		// } else {
		// 	Alerts.show('Unsuccessful, paste is invalid or corrupt.');
		// }
		return false;
	}
}
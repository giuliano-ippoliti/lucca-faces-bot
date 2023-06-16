(function() {
    
  function initHashNames() {
	  const hashTable = {}; //possible d'alimenter manuellement ici
	  
	  return hashTable;
  }
  
  function manageGame() {
	
	setTimeout(function() {
		var btns = document.getElementsByTagName('button');

		for (let i = 0; i < btns.length; i++) {
		  if (btns[i].textContent === 'Rejouer') {
			var boutonTrouve = btns[i];
			
			boutonTrouve.click();
			
			setTimeout(function() {
				var divElement = document.querySelector('.rotation-loader');
				//console.log('divElement: ' + divElement);
				if (divElement != null) {
					console.log('New Game');
					divElement.click();
				}
			}, 3000);
			
			break;
		  }
		}
	}, 5000);

  }

  // Remplace la fonction d'origine par une nouvelle implémentation
  function newXHR() {
    var xhr = new originalXHR();

    // Ajoute un gestionnaire d'événement pour les appels réseau
    xhr.addEventListener('load', function() {

      if (xhr.responseURL.includes('next')) {
	    var rep = JSON.parse(xhr.response);
		
		suggestions = rep.suggestions;
		
		var fullURL = 'https://xxxxxxx.ilucca.net' + rep.imageUrl;
		
		fetch(fullURL)
		  .then(response => {
			if (response.ok) {
			  var faceImg = response.blob();
			  return faceImg; // Récupérer les données de l'image sous forme de blob
			} else {
			  throw new Error("Erreur lors de la récupération de l'image.");
			}
		  })
		  .then(imageBlob => {
			blobSize = imageBlob.size; // Obtenir la taille du blob
			
			setTimeout(function() {
				buttons = document.querySelectorAll('.answer');

				buttons = Array.from(buttons);

				if (blobSize in HashNames) {
					for (const correctName in HashNames[blobSize]) {
						
						var found = -1;
						for (let i = 0; i <= 3; i++) {
							var txtButton = buttons[i].textContent.toLowerCase();
							if (txtButton.includes(correctName.toLowerCase())) {
								found = i;
								buttons[i].click();
								manageGame();
							}
						}
						if (found == -1) {
							// je clique sur le premier bouton, puis j'utilise la réponse à "guess" pour l'apprentissage
							buttons[0].click();
							manageGame();
						}
					}
				}
				else {			
					// click d'office sur le 1er
					buttons[0].click();
					manageGame();
				}
			}, 30); // on peut augmenter le timeout si la connexion réseau n'est pas très forte
		  })
		  .catch(error => {
			console.log("Une erreur s'est produite : " + error.message);
		  });
			
      }
	  else if (xhr.responseURL.includes('guess')) {
		var rep = JSON.parse(xhr.response);
		correctSuggestionId = rep.correctSuggestionId;
		var score =  rep.score;
		console.log(score);
		
		for (let i = 0; i <= 3; i++) {
			if (suggestions[i].id == correctSuggestionId) {

				if (blobSize in HashNames) {
					HashNames[blobSize][suggestions[i].value] = 1;
				}
				else {
					HashNames[blobSize] = {};	// initialisation
					HashNames[blobSize][suggestions[i].value] = 1;
				}
			}
		}
	  }

    });

    return xhr;
  }

  var originalXHR = window.XMLHttpRequest;

  window.XMLHttpRequest = newXHR;

  const HashNames = initHashNames();
  console.log(HashNames);
  
  var blobSize;
  var buttons;
  var suggestions;
  var correctSuggestionId;

})();
